from rest_framework import serializers

from follow.models import Follow
from user.serializers import UserSerializer


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = []


class UserFollowsSerializer(serializers.ModelSerializer):
    follows = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['follows', 'followed']


class UserFollowedSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['follower', 'followed']
