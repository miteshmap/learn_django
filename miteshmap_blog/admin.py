from django.contrib import admin
from miteshmap_blog.models import MiteshmapBlog, MiteshmapBlogTags, MiteshmapBlogWebsites

# Register your models here.
# admin.site.register(MiteshmapBlog)

@admin.register(MiteshmapBlog)
class MiteshmapBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'modified', 'is_published')
    list_filter = ('user', 'created', 'modified', 'is_published')
    search_fields = ('title',)
    date_hierarchy = 'created'
    prepopulated_fields = {'alias': ('title',)}

    # def published_status(self, obj):
    #     if (obj.is_published):
    #         return 'yes'
    #     else:
    #         return 'No'

# admin.site.register(MiteshmapBlog, MiteshmapBlogAdmin)
admin.site.register(MiteshmapBlogTags)
admin.site.register(MiteshmapBlogWebsites)
