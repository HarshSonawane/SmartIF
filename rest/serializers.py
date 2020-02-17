from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Profile


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for object author info"""

    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']


class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'