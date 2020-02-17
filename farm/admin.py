from django.contrib import admin
from .models import Farm, WaterResource, Soil, Plots, Ploting, Reports

admin.site.register(Farm)
admin.site.register(WaterResource)
admin.site.register(Soil)
admin.site.register(Plots)
admin.site.register(Ploting)
admin.site.register(Reports)