from rest_framework import serializers
from.models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserRegister
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'

