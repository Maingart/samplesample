from rest_framework import serializers

from tweet.models import Tweet
from user.serializers import UserSerializer


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['url', 'id', 'text', 'photo', 'created', 'author']
