from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import os
import random
from PIL import Image

from user.models import Address
from crop.models import Crop


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_file_path(instance, filename):
    new_filename = random.randint(1, 3231546414654785)
    name, ext =get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "posts/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Soil(models.Model):
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class WaterResource(models.Model):
    PRIMARY = 1
    SECONDARY = 2
    TYPE_CHOICES = (
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
    )

    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    volume          = models.IntegerField() #in liters
    depth           = models.IntegerField() #in feets
    diameter        = models.IntegerField() #in feets
    income_rate     = models.IntegerField() #liter per minute
    available_water = models.IntegerField() #in liter
    type            = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    is_active       = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Owner - ' + str(self.owner.first_name) + ' ' + str(self.owner.last_name) + ' - ' + str(self.volume) + ' Litres'

class Farm(models.Model):
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    soil            = models.ForeignKey(Soil, on_delete=models.DO_NOTHING)
    location        = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    water_resource  = models.ForeignKey(WaterResource, on_delete=models.DO_NOTHING)
    area            = models.DecimalField(default=000.0, max_digits=300, decimal_places=2)
    is_active       = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Owner - ' + str(self.owner.first_name) + ' ' + str(self.owner.last_name) + ' Area - ' + str(self.area) + ' Acres.'


class Plots(models.Model):
    FULL = 1
    HALF = 2
    AREA_CHOICES = (
        (FULL, 'Full'),
        (HALF, 'Half'),
    )
    farm            = models.ForeignKey(Farm, on_delete=models.CASCADE)
    area            = models.PositiveSmallIntegerField(choices=AREA_CHOICES , default=1)
    is_active       = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Owner - ' + str(self.farm.owner.first_name) + ' ' + str(self.farm.owner.last_name) + ' - ' + str(self.area) + ' Acres.'


class Ploting(models.Model):
    plot            = models.ForeignKey(Plots, on_delete=models.CASCADE)
    crop            = models.ForeignKey(Crop, on_delete=models.CASCADE)
    is_active       = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Plotted  - ' + str(self.crop.name) + ' on  ' + str(self.created) + ' at ' + str(self.plot)


class Reports(models.Model):
    added_by        = models.ForeignKey(User, on_delete=models.CASCADE)
    ploting         = models.ForeignKey(Ploting, on_delete=models.CASCADE)
    file            = models.ImageField(upload_to=upload_file_path)
    remark          = models.CharField(max_length=255, null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Report for  - ' + str(self.ploting.crop) + ' is added by ' + str(self.added_by)