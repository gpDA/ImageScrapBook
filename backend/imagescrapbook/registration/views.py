from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from main.permissions import IsOwnerOrReadOnly
#from accounts.api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Image
from main.serializers import ImageSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import  User

import json

def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True

class UserAPIView(generics.ListAPIView):
    permission_classes              = [] #[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes          = [] #[SessionAuthentication]
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

    permission_classes          = [] #[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]
    authentication_classes      = [] #[SessionAuthentication] #OR Json Web Token Authentication

    queryset                    = User.objects.all()
    #queryset                    = User.objects.filter(is_active=True)
    serializer_class            = UserSerializer
    lookup_field                = 'username' #'id' later





    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)