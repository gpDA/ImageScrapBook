from rest_framework import serializers
#from rest_framework.validators import UniqueValidator
#from django.contrib.auth.models import User
from main.models import Image, Tag
'''
Serializers --> JSON
Serializers --> Validation data
'''



class ImageSerializer(serializers.ModelSerializer):

    #ReadonlyField is untyped
    #NESTED SERIALIZER
    
    #owner       = serializers.ReadOnlyField(source='user.username')
    #owner      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Image
        fields = [
            'id',
            'user',
            'title',
            'image',
            'thumbnail_url',
            'timestamp',
            'privacy'
        ]
    def validate(self, data):
        title = data.get('title', None)
        image = data.get('image', None)
        thumbnail_url = data.get('thumbnail_url', None)
        if title == '':
            title = None
        if thumbnail_url == '':
            thumbnail_url = None

        #image is None
        if title is None and image is None and thumbnail_url is None:
            raise serializers.ValidationError('title, image, or thumbnail url is required.')
        return data

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    '''
    def get_owner(self, obj):
        qs = User.objects.filter(user=obj)
        return UserSerializer(qs, many=True).data        
    '''


class TagSerializer(serializers.ModelSerializer):

    #images      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tag
        fields = [
            'id',
            'tagnames',
            #'images'

        ]
    def validate(self, data):
        tagname = data.get('tagnames', None)
        if tagname == '':
            tagname = None

        if tagname is None:
            raise serializers.ValidationError('tagname is required.')
        return data