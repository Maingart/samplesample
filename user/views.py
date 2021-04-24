from django.contrib.auth.models import User

from rest_framework import viewsets

from user.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API User information
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'
