from rest_framework import serializers
from main.models import Image, Sharing
from django.contrib.auth.models import User
from registration.serializers import UserSerializer
#from main.serializers import RegisterSerializer
import thumbnail
import uuid
import boto3
import sys
from django.contrib.sessions.models import Session
'''
Serializers --> JSON
Serializers --> Validation data
'''

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class ImageCreateSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    # user = self.request.user
    # user = User.objects.get(pk=uid).id



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

        # user requesting
        
        # user requesting

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
    