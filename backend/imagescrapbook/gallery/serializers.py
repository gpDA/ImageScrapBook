
from rest_framework import serializers
from main.models import Image, Sharing
from django.contrib.auth.models import User
from registration.serializers import UserSerializer
from main.serializers import ImageSerializer
from main.serializers import ImageReadSerializer

class SharingSerializer(serializers.ModelSerializer):

    image          = serializers.SerializerMethodField(read_only=True)
    shared_to      = serializers.SerializerMethodField(read_only=True)
    shared_by      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Sharing
        fields = '__all__'

    
    def get_image(self,obj):
        qs = Image.objects.filter(sharing_image=obj)
        #qs = Image.objects.all()
        return ImageReadSerializer(qs, many=True).data
    
    def get_shared_by(self,obj):
        qs = User.objects.filter(sharing_shared_by=obj)
        return UserSerializer(qs, many=True).data        

    def get_shared_to(self,obj):
        qs = User.objects.filter(sharing_shared_to=obj)
        return UserSerializer(qs, many=True).data        

class SharingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sharing
        fields = '__all__'