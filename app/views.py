from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

from app.forms import LoginForm, UserForm


def index(request):
    return render(request, 'index.html')


@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {"users": users})


@login_required
def users_create(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users'))

    return render(request, 'users/create.html', {"form": form})


def login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('profile.edit'))
            form.add_error('password', 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


@login_required
def profile_edit(request):
    return render(request, 'profile/edit.html')
