from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import AdminUserCreateForm, AdminUserUpdateForm, AdminProductUpdateForm, AdminCategoryUpdateForm
from mainapp.models import Product, Category


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context


class UserList(SuperUserOnlyMixin, ListView):
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        result = queryset.order_by('-is_active', '-is_superuser')
        return result


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        user_form = AdminUserCreateForm()

    context = {
        'title': 'User/Создание',
        'form': user_form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_form = AdminUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        user_form = AdminUserUpdateForm(instance=user)

    context = {
        'title': 'User/Редактирование',
        'form': user_form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:index'))

    context = {
        'title': 'User/Удаление',
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'Admin/Категории',
        'object_list': categories,
    }
    return render(request, 'adminapp/categories_list.html', context)


class CategoryCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = Category
    success_url = reverse_lazy('adminapp:categories')
    form_class = AdminCategoryUpdateForm
    page_title = 'Категории/Создание'


class CategoryUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = Category
    success_url = reverse_lazy('adminapp:categories')
    form_class = AdminCategoryUpdateForm
    page_title = 'Категории/Редактирование'


class CategoryDeleteView(SuperUserOnlyMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('adminapp:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return super().get_success_url()


@user_passes_test(lambda u: u.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    object_list = category.product_set.all()
    context = {
        'title': f'Категория {category.name}/Продукты',
        'category': category,
        'object_list': object_list,
    }
    return render(request, 'adminapp/category_products_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'adminapp:category_products',
                kwargs={'pk': category.pk}))
    else:
        form = AdminProductUpdateForm(initial={'category': category})

    context = {
        'title': 'Продукты/Создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/../templates/mainapp/category_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:category_products', kwargs={'pk': product.category.pk}))
    else:
        form = AdminProductUpdateForm(instance=product)

    context = {
        'title': 'Продукты/Редактирование',
        'form': form,
        'category': product.category,
    }
    return render(request, 'adminapp/../templates/mainapp/category_form.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        obj.is_active = False
        obj.save()
        return HttpResponseRedirect(reverse('adminapp:category_products', kwargs={'pk': obj.category.pk}))

    context = {
        'title': 'Продукты/Удаление',
        'object': obj,
    }
    return render(request, 'adminapp/product_delete.html', context)


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'


def db_profile_by_type(prefix, query_type, queries):
    update_queries = list(filter(lambda x: query_type in x['sql'], queries))
    print(f'db_profile {query_type} for {prefix}:')
    [print(query['sql']) for query in update_queries]


@receiver(post_save, sender=Category)
def product_is_active_update_productcategory_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)

        db_profile_by_type(sender, 'UPDATE', connection.queries)
