from django.urls import path
from django.contrib.auth.views import login, logout
from accounts.views import *

urlpatterns = [
    path('', AccountHome.as_view()),
    path('register/', AccountRegister.as_view(), name="register"),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('profile/', AccountProfileView.as_view(), name="profile_view"),
    path('profile/edit/', AccountProfileEdit.as_view(), name="profile_edit"),
    path('profile/password/', AccountProfilePasswordChange.as_view(), name="profile_password_change"),
]
