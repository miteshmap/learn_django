from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html', {"title": "Hello world!", "numbers": [1, 2, 3]})