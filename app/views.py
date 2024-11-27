from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return redirect(reverse('index') + "?after=logout")


def profile_edit(request):
    return render(request, 'profile/edit.html')
