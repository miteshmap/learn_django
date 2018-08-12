from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegistrationFrom, 
    ProfileEditForm, 
    ProfilePasswordChangeForm
)
from django.contrib.auth.models import User
from django.views import View

class AccountHome(View):
    def get(self, request):
        return render(request, 'accounts/home.html', {"title": "Hello world!", "numbers": [1, 2, 3]})

class AccountRegister(View):
    """
    Register: (new)class based way of handling register view.
    """
    template_name = 'accounts/register.html'
    from_class = RegistrationFrom
    def get(self, request):
        return render(request, self.template_name, {'form': self.from_class()})
    
    def post(self, request):
        form = self.from_class(request.POST)
        if (form.is_valid()):
            form.save()
            redirect('/account/login')
        return render(request, self.template_name, {'form': form})

class AccountProfileView(View):
    def get(self, request):
        return render(request, "accounts/profile.html", {'user': request.user})

class AccountProfileEdit(View):
    form = ProfileEditForm

    def get(self, request):
        form = ProfileEditForm
        return render(request, "accounts/profile_edit.html", {'form': self.form(instance=request.user)})
    
    def post(self, request):
        form = self.form(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')        

class AccountProfilePasswordChange(View):
    form = ProfilePasswordChangeForm
    
    def get(self, request):
        return render(request, "accounts/profile_password_change.html", {'form': self.form(user=request.user)})
    
    def post(self, request):
        form = self.form(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
