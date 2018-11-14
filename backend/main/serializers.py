from rest_framework import serializers
from main.models import Image, Tags
'''
Serializers --> JSON
Serializers --> Validation data
'''

class ImageSerializer(serializers.ModelSerializer):
    #user        = UserPublicSerializer(read_only=True)

    class Meta:
        model = Image
        fields = [
            'id',
            #'user',
            'title',
            'image',
            'thumbnail_url',
        ]
    def validate(self, data):
        title = data.get('title', None)
        image = data.get('image', None)
        thumbnail_url = data.get('thumbnail_url', None)
        if title == '':
            title = None
        if thumbnail_url == '':
            thumbnail_url = None

        if title is None and image is None and thumbnail_url is None:
            raise serializers.ValidationError('title, image, or thumbnail url is required.')
        return data

'''
class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = [
            'id',
            'tagname',
            'images',

        ]
    def validate(self, data):
        tagname = data.get('tagname', None)
        if tagname == '':
            tagname = None

        if tagname is None:
            raise serializers.ValidationError('tagname is required.')
        return data
'''