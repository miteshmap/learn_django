from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationFrom

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
