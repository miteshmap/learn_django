from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.home),
    path('register', views.register, name="register"),
    path('login', login, {'template_name': 'accounts/login.html'}),
    path('profile', views.profile_view, name="profile_view"),
    path('profile/edit', views.profile_edit, name="profile_edit"),
    path('password', views.profile_password_change, name="profile_password_change"),
]
