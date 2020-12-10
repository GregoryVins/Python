from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import SchoolUserLoginForm, SchoolUserRegisterForm, SchoolUserUpdateForm


def login(request):
    """USER LOGIN."""
    if request.method == 'POST':
        form = SchoolUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = SchoolUserLoginForm()

    context = {
        'title': 'вход',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    """LOGOUT USER."""
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    """REGISTER A NEW USER LOGIC."""
    if request.method == 'POST':
        form = SchoolUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = SchoolUserRegisterForm()

    context = {
        'title': 'register',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def update(request):
    """UPDATE USER."""
    if request.method == 'POST':
        form = SchoolUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:update'))
    else:
        form = SchoolUserUpdateForm(instance=request.user)

    context = {
        'title': 'Профиль',
        'form': form,
    }
    return render(request, 'authapp/update.html', context)
