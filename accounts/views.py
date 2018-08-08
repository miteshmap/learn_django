from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationFrom, ProfileEditForm, ProfilePasswordChangeForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html', {"title": "Hello world!", "numbers": [1, 2, 3]})

def register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if (form.is_valid()):
            form.save()
            redirect('/account/login')
    else:
        form = RegistrationFrom()

    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def profile_view(request):
    return render(request, "accounts/profile.html", {'user': request.user})

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form}
        return render(request, "accounts/profile_edit.html", args)

def profile_password_change(request):
    if request.method == 'POST':
        form = ProfilePasswordChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('/account/profile')
    else:
        form = ProfilePasswordChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, "accounts/profile_password_change.html", args)
