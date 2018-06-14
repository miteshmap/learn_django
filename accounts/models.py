from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    """
    User profile class to have additional fields for users.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default= '')
    city = models.CharField(max_length=100, default='')
    website = models.URLField()
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    """
    Create user profile when admin creates a user that's why it should
    be triggered in post_save of User.
    """
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)