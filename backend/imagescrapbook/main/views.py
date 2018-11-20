from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
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

class ImageAPIDetailView(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.RetrieveAPIView):
    permission_classes          = [] #[permissions.IsAuthenticatedOrReadOnly, ]
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

class ImageAPIView(mixins.CreateModelMixin,
                        generics.ListAPIView):
    permission_classes              = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes          = [SessionAuthentication] #Json Web Token Authentication
    #queryset                        = Image.objects.all()
    serializer_class                = ImageSerializer

    def get_queryset(self):
        qs = Image.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query) #query by title?? or multiple queries
        return qs

    #logic to save S3 and rabbit needs to set in this function
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
