from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from user.models import Profile

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer