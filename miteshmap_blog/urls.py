from django.urls import path
from miteshmap_blog.views import MiteshmapBlogView

urlpatterns = [
    path('list', MiteshmapBlogView.as_view()),
]
