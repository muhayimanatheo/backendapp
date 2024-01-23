from rest_framework import serializers
from.models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '_all_'