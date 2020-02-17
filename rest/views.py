from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from user.models import Profile
from farm.models import Farm

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class FarmsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Farm.objects.all()
    serializer_class = serializers.FarmsSerializer