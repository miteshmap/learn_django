from django.shortcuts import render, HttpResponse, redirect
from django.views import View, generic
from miteshmap_blog.models import MiteshmapBlog

# Create your views here.
class MiteshmapBlogListView(generic.ListView):
    # def get(self, request):
    model = MiteshmapBlog
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    # queryset = MiteshmapBlog.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'miteshmap_blog/blog-list.html'

class MiteshmapBlogDetailView(generic.DetailView):
    model = MiteshmapBlog
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    slug_field = 'alias'
    query_pk_and_slug = True
    template_name = 'miteshmap_blog/blog-detail.html'
