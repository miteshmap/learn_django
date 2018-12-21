from django.urls import path, re_path
from miteshmap_blog.views import MiteshmapBlogListView, MiteshmapBlogDetailView

urlpatterns = [
    path('', MiteshmapBlogListView.as_view(), name='blog-list'),
    path('<int:pk>', MiteshmapBlogDetailView.as_view(), name='blog-detail'),
    re_path('^(?P<slug>[\w-]+)/*$', MiteshmapBlogDetailView.as_view(), name='blog-detail-slug'),
]
