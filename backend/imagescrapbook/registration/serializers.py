from rest_framework import serializers

from main.models import Image
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from main.serializers import ImageSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_auth.app_settings import (
                                    create_token)
# from .models import TokenModel


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = DefaultTokenModel
        fields = ('key',)


class RegisterSerializer(serializers.ModelSerializer):

    #images      = serializers.SerializerMethodField(read_only=True)

    username = serializers.CharField(
        max_length=30,
        min_length=6,
        required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    # password1 = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     if data['password'] != data['password1']:
    #         raise serializers.ValidationError(_("The two password fields didn't match."))
    #     return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        create_token(self.token_model, user, serializer)
        return user
    
    def get_images(self, obj):
        qs = Image.objects.filter(user=obj).order_by("-timestamp")[:10]
        return ImageSerializer(qs, many=True).data        
    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')#, 'images')

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     return user


class UserSerializer(serializers.ModelSerializer):
    #Since `images` is a reverse relationship on the User model, it will not be included by default
    #images      = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())
    images      = serializers.SerializerMethodField(read_only=True)

    email       = serializers.EmailField(required=True,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    username    = serializers.CharField(max_length=32)
    password1    = serializers.CharField(min_length=8, write_only=True)
    password2    = serializers.CharField(min_length=8, write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password1'])
        return user
      

    
    def get_images(self, obj):
        qs = Image.objects.filter(user=obj).order_by("-timestamp")[:10]
        return ImageSerializer(qs, many=True).data
    

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(("The two password fields didn't match."))
        return data    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password1', 'password2', 'images')      