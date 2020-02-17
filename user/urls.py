from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='user_home'),
    path('profile', views.complete_profile, name='profile'),
    path('address/add/', views.add_address, name='add_address'),
    path('add/water/resource/', views.add_water_resource, name='add_water_resource'),
    path('farm/add/', views.add_farm, name='add_farm'),
    path('plots/add/', views.add_plot, name='add_plot'),
    path('ploting/add/', views.add_ploting, name='add_ploting'),
    path('ploting/<int:id>/', views.planting_details, name='ploting_details'),
    path('ploting/upload/', views.upload, name='upload_image'),
    path('become/biologist/', views.become_biologist, name='become_biologist'),
    path('', views.index, name='user_home'),
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
