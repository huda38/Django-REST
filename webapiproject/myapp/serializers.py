from rest_framework import serializers
from myapp.models import User, Color

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    fav_colorname=serializers.CharField(max_length=100)
    
    
    def create(self, validated_data):
        return User.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    
