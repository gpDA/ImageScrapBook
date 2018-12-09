
from rest_framework import serializers
from main.models import Image, Tag, Sharing
# from django.contrib.auth.models import User
# from registration.serializers import UserSerializer
from main.serializers import ImageSerializer

class SharingSerializer(serializers.ModelSerializer):

    images      = serializers.SerializerMethodField(read_only=True)
    #users      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Sharing
        fields = '__all__'

    
    def get_images(self,obj):
        qs = Image.objects.all()
        return ImageSerializer(qs, many=True).data
    '''
    def get_users(self,obj):
        qs = User.objects.all()
        return UserSerializer(qs, many=True).data        
    ''' 