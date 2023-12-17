from django.contrib.auth.models import User
from rest_framework import serializers


# class Usermodel:
#     def __init__(self, )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
