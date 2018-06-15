from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('login', login, {'template_name': 'accounts/login.html'}),
]
