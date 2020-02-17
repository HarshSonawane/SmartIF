from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('farms', views.FarmsViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]