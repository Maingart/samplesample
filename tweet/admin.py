from django.contrib import admin

# Register your models here.
from tweet.models import Tweet

admin.site.register(Tweet)
