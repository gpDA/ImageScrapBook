from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
'''
Serializers --> JSON
Serializers --> Validation data
'''

class UserSerializer(serializers.ModelSerializer):
    #Since `images` is a reverse relationship on the User model, it will not be included by default
    #images      = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    email       = serializers.EmailField(required=True, 
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    username    = serializers.CharField(max_length=32)
    password    = serializers.CharField(min_length=8, write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        return user



    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
