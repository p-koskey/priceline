from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', blank=True)
    name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = CloudinaryField('image')


    def __str__(self):
            return f'{self.user.username} profile'
            
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()