from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly

from tweet.models import Tweet


class IsAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    The request is authenticated as a author, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj: Tweet):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.author == request.user)
