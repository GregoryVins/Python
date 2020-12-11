from django.shortcuts import render, get_object_or_404

from mainapp.models import Category, Product


def index(request):
    categories = Category.objects.all()
    context = {
        'title': 'Главная',
        'categories': categories,
    }
    return render(request, 'mainapp/index.html', context)


def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.product_set.all()

    context = {
        'title': f'Категория {category.name}',
        'category': category,
        'products': products,
    }

    return render(request, 'mainapp/category_products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': 'Продукт',
        'product': product,
    }
    return render(request, 'mainapp/product_detail.html', context)
