from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import os

from user.models import Address

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
    efficiency      = models.IntegerField() #in liters
    income_rate     = models.IntegerField() #liter per minute
    type            = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=1)
    is_active       = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.owner + str(self.volume) + self.get_type_display

class Farm(models.Model):
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    location        = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    water_resource  = models.ForeignKey(WaterResource, on_delete=models.DO_NOTHING)
    area            = models.DecimalField(default=000.0, max_digits=300, decimal_places=2)
    is_active       = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.owner + str(self.area)

