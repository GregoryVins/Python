from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name="index"),
    path('category/<int:pk>', mainapp.category_products, name="category"),
    path('product/detail/<int:pk>', mainapp.product_detail, name="product_detail")
]
