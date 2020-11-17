from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm
from authapp.models import User


def index(request):
    """
    Авторизация пользователя в системе как персонал и супербюзер.
    Если пользователя нет, то он будет создан.
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            auth.login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    print(request.user)
    return render(request, 'authapp/index.html', context)


def logout(request):
    """Выход из системы"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:login'))
