from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import os

from user.models import Address

class Crop(models.Model):
    WINTER = 1
    SUMMER = 2
    RAINY = 3
    SEASON_CHOICES = (
        (WINTER, 'Winter'),
        (SUMMER, 'Summer'),
        (RAINY , 'Rainy'),
    )
    name                = models.CharField(max_length=255)
    duration            = models.IntegerField() #days
    season              = models.PositiveSmallIntegerField(choices=SEASON_CHOICES)
    water_requirement   = models.IntegerField() # liter per squarefit per week
    water_reapeat       = models.IntegerField() #days
    height              = models.IntegerField() #feet
    width               = models.IntegerField() #feet
    is_food             = models.BooleanField(default=True)
    is_active           = models.BooleanField(default=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name