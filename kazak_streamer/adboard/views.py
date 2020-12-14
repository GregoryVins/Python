from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from adboard.forms import AdCreateForm
from adboard.models import AdCategory, Ad


def get_all_categories():
    return AdCategory.objects.all()


def ad_main_page(request, pk=0):
    if pk == 0:
        products = Ad.objects.all()
    else:
        category = get_object_or_404(AdCategory, pk=pk)
        products = category.ad_set.all()

    context = {
        'title': 'Доска объявлений',
        'categories': get_all_categories,
        'products': products,
    }
    return render(request, 'adboard/ads.html', context)


def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    context = {
        'categories': get_all_categories,
        'ad': ad,
        'title': 'Добавить объявление'
    }
    return render(request, 'adboard/ad_detail.html', context)


def add_ad(request):
    if request.method == 'POST':
        form = AdCreateForm(request.POST, )
        if form.is_valid():
            Ad.objects.create(
                ad_category=get_object_or_404(AdCategory, pk=request.POST['ad_category']),
                author=request.user,
                name=request.POST['name'],
                description=request.POST['description'],
                price=request.POST['price'],
                city=request.POST['city'],
                year=request.POST['year'],
            )

    else:
        form = AdCreateForm()

    context = {
        'title': 'Добавить объявление',
        'form': form,
    }
    return render(request, 'adboard/add_ad.html', context)
