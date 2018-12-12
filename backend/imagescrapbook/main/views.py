from rest_framework import generics, permissions
from main.models import Image
from main.serializers import ImageCreateSerializer, ImageReadSerializer, ImageSerializer


import json


def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True


class ImageCreateAPIView(generics.CreateAPIView):
    permission_classes              = []
    queryset                        = Image.objects.all()
    serializer_class                = ImageCreateSerializer

    def get_queryset(self):
        qs = Image.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query) #query by title?? or multiple queries
        return qs


class ImageAPIView(generics.ListAPIView):
    permission_classes              = []
    queryset                        = Image.objects.all()
    serializer_class                = ImageSerializer

    def get_queryset(self):
        qs = Image.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query) #query by title?? or multiple queries
        return qs


class ImageReadAPIView(generics.ListAPIView):
    permission_classes              = [permissions.IsAuthenticated]
    queryset                        = Image.objects.all()
    serializer_class                = ImageReadSerializer

    def get_queryset(self):
        qs = Image.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query) #query by title?? or multiple queries
        return qs


class ImageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes          = []

    queryset                    = Image.objects.all()
    serializer_class            = ImageSerializer
    lookup_field                = 'id' #slug for later

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
