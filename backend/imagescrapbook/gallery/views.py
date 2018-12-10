
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token

from rest_framework import generics, mixins, permissions
from main.models import Sharing
from gallery.serializers import SharingSerializer
from gallery.serializers import SharingCreateSerializer

class SharingAPIView(generics.ListAPIView):
    permission_classes              = [] #[permissions.IsAuthenticated,]
    queryset                        = Sharing.objects.all()
    serializer_class                = SharingSerializer    

class SharingCreateAPIView(generics.CreateAPIView):
    permission_classes              = [] #[permissions.IsAuthenticated,]
    queryset                        = Sharing.objects.all()
    serializer_class                = SharingCreateSerializer    
