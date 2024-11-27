from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('users/create', views.users_create, name='users.create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/edit', views.profile_edit, name='profile.edit'),
]
