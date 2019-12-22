from django.contrib import admin
from django.urls import path

from . import views
from products.views import ProductListView

urlpatterns = [

    path('users/', ProductListView.as_view(), name='users_add'),
    path('users/login', views.login_user, name='login'),
    path('users/logout', views.logout_user, name='logout'),
    path('users/register', views.register_user, name='register'),
]
