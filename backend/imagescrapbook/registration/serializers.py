from rest_framework import serializers

from main.models import Image
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
#from main.serializers import ImageSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_auth.app_settings import (
                                    create_token)
# from .models import TokenModel


'''ToeknSerializer'''
class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = DefaultTokenModel
        fields = ('key',)


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        max_length=30,
        min_length=6,
        required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     return user


class UserSerializer(serializers.ModelSerializer):

    email       = serializers.EmailField(required=True,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    username    = serializers.CharField(max_length=32)
    password    = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')