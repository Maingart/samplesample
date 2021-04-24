from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    text: str = models.TextField(max_length=280)
    photo: str = models.CharField(max_length=200, blank=True)
    created: datetime = models.DateTimeField(auto_now_add=True)
    author: User = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
