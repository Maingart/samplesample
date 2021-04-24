from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins

from follow.models import Follow
from follow.serializers import FollowSerializer, UserFollowsSerializer, \
    UserFollowedSerializer


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Follow.objects
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        follows = User.objects.get(username=self.kwargs[self.lookup_field])
        serializer.save(
            follower=self.request.user,
            follows=follows
        )

    def get_object(self):
        return self.queryset.filter(
            follower=self.request.user,
            follows__username=self.kwargs[self.lookup_field]
        )


class UserFollowsViewsSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Follow.objects
    serializer_class = UserFollowsSerializer

    def get_queryset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(follower__username=username)


class UserFollowedViewsSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Follow.objects
    serializer_class = UserFollowedSerializer

    def get_queryset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(follows__username=username)
