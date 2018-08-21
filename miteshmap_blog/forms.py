from django import forms
from django.contrib.auth.models import User
from miteshmap_blog.models import MiteshmapBlog, MiteshmapBlogTags, MiteshmapBlogWebsites

class MiteshmapBlogCreate():
    
    class Meta:
        model = MiteshmapBlog
        fields = (
            'title',
            'description',
            # 'tags',
            'websites',
            'create',
            'is_published',
            'tags',
            'websites',
        )

    def save(self, commit=True):
        pass
        # user = super(RegistrationFrom, self).save(commit=False)
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data["password1"])

        # if commit:
        #     user.save()

        # return user