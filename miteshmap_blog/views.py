from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.
class MiteshmapBlogView(View):
    def get(self, request):
        return render(request, 'templates/blog-view.html')
        