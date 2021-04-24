from rest_framework import viewsets, permissions

from tweet.models import Tweet
from tweet.permissions import IsAuthorOrReadOnly
from tweet.serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserTweetsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tweet.objects
    serializer_class = TweetSerializer

    def get_queryset(self):
        return self.queryset.filter(
            author__username=self.kwargs['parent_lookup_username']
        )


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tweet.objects
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(
            author__followers__follower=user
        )
