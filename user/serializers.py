from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']
        extra_kwargs = {'url': {'lookup_field': 'username'}}
