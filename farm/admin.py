from django.contrib import admin
from .models import Farm, WaterResource, Soil

admin.site.register(Farm)
admin.site.register(WaterResource)
admin.site.register(Soil)