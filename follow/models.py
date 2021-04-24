from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    follower = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='follows'
    )
    follows = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='followers'
    )
    followed = models.DateTimeField(auto_now_add=True)
