from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
#from accounts.api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Image
from main.serializers import ImageSerializer

import json

def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True
     

#generics.ListAPIView,mixins.CreateModelMixin
class ImageAPIView(generics.ListCreateAPIView):
    permission_classes              = [] #[permissions.IsAuthenticatedOrReadOnly,]
    authentication_classes          = [] #[SessionAuthentication] #Json Web Token Authentication
    queryset                        = Image.objects.all()
    serializer_class                = ImageSerializer

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

#mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView    
class ImageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly,] #[permissions.IsAuthenticatedOrReadOnly, ]
    authentication_classes      = [] #[SessionAuthentication] #OR Json Web Token Authentication

    queryset                    = Image.objects.all()
    serializer_class            = ImageSerializer
    lookup_field                = 'id' #slug for later
    '''
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    '''