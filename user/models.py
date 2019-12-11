from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import os


class Address(models.Model):

    STATE_CHOICES = (
    ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
    ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry"))


    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    line_1          = models.CharField(max_length=250)
    town            = models.CharField(max_length=250, blank=True, null=True)
    landmark        = models.CharField(max_length=250, blank=True, null=True)
    city            = models.CharField(max_length=250)
    district        = models.CharField(max_length=250)
    state           = models.CharField(choices=STATE_CHOICES, max_length=255)
    pin             = models.IntegerField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line_1 + self.city

class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER , 'Other'),
    )

    FARMER = 1
    DOCTOR = 2
    SHOP = 3
    GENDER_CHOICES = (
        (FARMER, 'Farmer'),
        (DOCTOR, 'Doctor'),
        (SHOP , 'Shop'),
    )
     
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image   = models.ImageField(upload_to='profile/%y/%m/%d/', blank=True)
    type            = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    status          = models.BooleanField(default=False)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

        

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

