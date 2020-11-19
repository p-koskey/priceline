from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from tinymce.models import HTMLField

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

class Bookings(models.Model):
    car_name = models.CharField(max_length=100)
    startdate = models.DateField(verbose_name=_('Start Date'),help_text='Borrowed is on ..',null=True,blank=False)
	returndate = models.DateField(verbose_name=_('Return Date'),help_text='will be returned on ...',null=True,blank=False)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return self.car_name

    @property
	def rent_days(self):
		days_count = ''
		startdate = self.startdate
		enddate = self.enddate
		if startdate > returndate:
			return
		dates = (enddate - returndate)
		return dates.days

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)

class Categories(models.Model):
    car_type= CharField(max_length=400)
    logo = CloudinaryField('image', null=True)
    description = HTMLField()
    name =models.CharField(max_length=100)
    email = models.EmailField()
    location =models.CharField(max_length=100)
    contact = PhoneNumberField()

    def __str__(self):
        return self.name