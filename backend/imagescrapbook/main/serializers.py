from rest_framework import serializers
from main.models import Image, Tag, Sharing
from django.contrib.auth.models import User
from registration.serializers import UserSerializer
#from main.serializers import RegisterSerializer
import thumbnail
import uuid
import boto3
import sys
'''
Serializers --> JSON
Serializers --> Validation data
'''

class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            'id',
            'user',
            'title',
            'image',
            'extension',
            'timestamp',
            'thumbnail_url',
            'imageurl',
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
        if title is None or image is None:
            raise serializers.ValidationError('title and image is required.')
        return data

    def create(self, validated_data):
        # Do processing
        image = validated_data['image']
        del validated_data['image']
        ext = validated_data['extension']
        # TODO: have a shared s3 obj instead of instantiating
        s3 = boto3.resource('s3', use_ssl=False, endpoint_url='http://minio:9000/')
        # TODO: check for collisions
        imguuid = uuid.uuid4()
        imgurl = f'{validated_data["user"].id}-{imguuid}.{ext}'
        s3.Object('image', imgurl).put(Body=image.file)
        validated_data['imageurl'] = imgurl
        obj = Image(**validated_data)
        obj.save()

        # Send task
        thumbnail.thumbnailify.delay(obj.id, imgurl, (200, 200))
        return obj



class ImageSerializer(serializers.ModelSerializer):

    #ReadonlyField is untyped
    #NESTED SERIALIZE

    user      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Image
        fields = [
            'id',
            'user',
            'title',
            'image',
            'extension',
            'timestamp',
            'thumbnail_url',
            'imageurl',
        ]
    
    
    def get_user(self,obj):
        qs = User.objects.filter(image=obj)
        #qs = Image.objects.filter(user=obj).order_by("-timestamp")[:10]
        return UserSerializer(qs, many=True).data

class ImageReadSerializer(serializers.ModelSerializer):

    #ReadonlyField is untyped
    #NESTED SERIALIZE

    class Meta:
        model = Image
        fields = [
            'id',
            'title',
            'image',
            'extension',
            'timestamp',
            'thumbnail_url',
            'imageurl',
        ]
    

class TagSerializer(serializers.ModelSerializer):

    #images      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tag
        fields = [
            'id',
            'tagname',
            #'images'

        ]

    def validate(self, data):
        tagname = data.get('tagname', None)
        if tagname == '':
            tagname = None

        if tagname is None:
            raise serializers.ValidationError('tagname is required.')
        return data
