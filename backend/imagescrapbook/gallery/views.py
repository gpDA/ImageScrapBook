
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
#from accounts.api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Sharing
from gallery.serializers import SharingSerializer

class SharingAPIView(generics.ListCreateAPIView):
    permission_classes              = [] #[permissions.IsAuthenticated,]
    #authentication_classes          = [] #[SessionAuthentication] #Json Web Token Authentication
    queryset                        = Sharing.objects.all()
    serializer_class                = SharingSerializer    
