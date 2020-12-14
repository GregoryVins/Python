from django.urls import path
import adboard.views as adboard

app_name = 'adboard'

urlpatterns = [
    path('<int:pk>/', adboard.ad_main_page, name='main_page'),
    path('ad/<int:pk>', adboard.ad_detail, name='ad_detail'),
    path('add/', adboard.add_ad, name='add_ad'),
]
