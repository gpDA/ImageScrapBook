from rest_framework.views import APIView
from django.conf import settings
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, permissions, status
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.response import Response
from main.permissions import IsOwnerOrReadOnly
#from accounts.api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Image
from main.serializers import ImageSerializer
from .serializers import RegisterSerializer, TokenSerializer, UserSerializer
from django.contrib.auth.models import  User
# from registration.models import TokenModel
# from rest_framework.authtoken.models import Token as DefaultTokenModel
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView

from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from rest_auth.utils import jwt_encode                                    

import json

# sensitive_post_parameters_m = method_decorator(
#     sensitive_post_parameters('password', 'password2')
# )
class RegisterView(generics.CreateAPIView): #generics.ListCreateAPIView
    serializer_class = RegisterSerializer
    permission_classes          = [] #[permissions.IsAuthenticatedOrReadOnly, ]
    # query = self.request.GET.get("q")
    queryset                        = User.objects.all()    
    token_model = Token

    # @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        # PROBLEM
        return TokenSerializer(user.auth_token).data

    # def save(self, *request):
    #     data = request.data
    #     print(data)
    #     # serializer = self.get_serializer(data=request.data)
    #     # # serializer.is_valid(raise_exception=True)
    #     # user = self.perform_create(serializer)
    #     # headers = self.get_success_headers(serializer.data)
    #     # return Response(self.get_response_data(user),
    #     #                 status=status.HTTP_201_CREATED,
    #     #                 headers=headers)

    def save(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)                        
        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)        

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     return Response(self.get_response_data(user),
    #                     status=status.HTTP_201_CREATED,
    #                     headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        create_token(self.token_model, user, serializer)
        return user                        




class UserAPIView(generics.ListAPIView):
    permission_classes              = [] #permissions.IsAuthenticated
    # authentication_classes          = [] #[SessionAuthentication]
    queryset                        = User.objects.all()
    serializer_class                = UserSerializer   

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                #print(token)
                json = serializer.data
                json['token'] = token.key
                print(json['token'])

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


#mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView
class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes          = [] #permissions.IsAuthenticated
    #authentication_classes      = [] #[SessionAuthentication] #OR Json Web Token Authentication

    queryset                    = User.objects.all()
    #queryset                    = User.objects.filter(is_active=True)
    serializer_class            = RegisterSerializer
    lookup_field                = 'username' #'id' later





    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
