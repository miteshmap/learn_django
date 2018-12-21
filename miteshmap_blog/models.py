from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

# Import regular expression.
import re

# class MiteshmapImage(models.Model):
#     image = models.ImageField(upload_to="images")
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey("content_type", "object_id")

class MiteshmapBlogTags(models.Model):
    """
    Tags for blogs.
    """
    term = models.CharField(max_length=100,)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.term

class MiteshmapBlogWebsites(models.Model):
    """
    Reference websites.
    """
    website = models.CharField(max_length=255, blank=True, null=True)
    # blog_id = models.ForeignKey(
    #     'blog.MiteshmapBlog',
    #     on_delete=models.CASCADE,
    #     related_name='blogs_MiteshmapBlogWebsites_related',
    #     related_query_name='blogs_MiteshmapBlogWebsites',
    #     null=True
    # )

    class Meta:
        db_table = 'websites'

    def __str__(self):
        return self.website

class MiteshmapBlog(models.Model):
    """
    Blog model to create fields.
    """
    title = models.CharField(max_length=255, default='')
    description = RichTextField(config_name='awesome_ckeditor')
    alias = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(MiteshmapBlogTags)
    modified = models.DateTimeField(default=timezone.now)
    website = models.ManyToManyField(MiteshmapBlogWebsites, blank=True)
    is_published = models.BooleanField(
        'published',
        default=True,
        help_text=_(
            'Designates whether this blog is published. '
            'Unselect this instead of deleting blogs.'
        ),
    )

    def get_tag_list(self):
        return re.split(" ", self.tags)

    def get_absolute_url(self):
        return reverse('miteshmap_blog:blog-detail-slug', args=[self.alias])
        # return '/blog/%s' % self.alias

    class Meta:
        db_table = 'blogs'
        ordering = ["-created"]

    def __str__(self):
        return self.title
