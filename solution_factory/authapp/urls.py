from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('', authapp.index, name='login'),
    path('logout/', authapp.logout, name='logout'),
]
