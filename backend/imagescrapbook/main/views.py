from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
#from accounts.api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Image
from main.serializers import ImageSerializer, UserSerializer
from django.contrib.auth.models import User

import json

def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True

class UserCreate(APIView):
    #create user

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(generics.ListAPIView):
    permission_classes              = [] #[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes          = [] #[SessionAuthentication]
    queryset                        = User.objects.all()
    serializer_class                = UserSerializer   



class UserAPIDetailView(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly,
                                    IsOwnerOrReadOnly,] #[permissions.IsAuthenticatedOrReadOnly, ]
    authentication_classes      = [] #[SessionAuthentication] #OR Json Web Token Authentication

    queryset                    = User.objects.all()
    serializer_class            = UserSerializer
    lookup_field                = 'id' #slug for later

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ImageAPIView(generics.ListAPIView,
                    mixins.CreateModelMixin):
    permission_classes              = [permissions.IsAuthenticatedOrReadOnly,] #[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes          = [] #[SessionAuthentication] #Json Web Token Authentication
    #queryset                        = Image.objects.all()
    serializer_class                = ImageSerializer

    #logic to save S3 and rabbit needs to set in this function
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        qs = Image.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query) #query by title?? or multiple queries
        return qs

    #otherwise, if we created image, there is no way of associating the user that created it
    #the User is not sent as part of the serialized representation, but is instead a property of the incoming request
    #OVERRIDE `perform_create()` method that allows us to modify how the instance save is managed
    def perform_create(self, serializer):
        # `create() method` has additional `owner` field (along with the validated data from the request)
        serializer.save(owner=self.request.user)

class ImageAPIDetailView(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly,] #[permissions.IsAuthenticatedOrReadOnly, ]
    authentication_classes      = [] #[SessionAuthentication] #OR Json Web Token Authentication

    queryset                    = Image.objects.all()
    serializer_class            = ImageSerializer
    lookup_field                = 'id' #slug for later

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)