from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from authapp.models import UserProfile


def login(request):
    """
    Авторизация пользователя в системе.
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'вход',
        'form': form,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    """
    Выход пользователя из системы.
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    """
    Регистрация пользователя в системе.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if UserProfile.objects.filter(nickname=request.POST['nickname']).count() != 0:
            return HttpResponseRedirect(reverse('auth:error'))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'регистрация',
        'form': form,
    }

    return render(request, 'authapp/register.html', context)


@login_required
def update(request):
    """
    Обновление пользователя в системе.
    """
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'title': 'обновление',
        'form': form,
    }

    return render(request, 'authapp/update.html', context)


def error(request):
    return render(request, 'authapp/nickname_error.html', {"title": 'error'})
