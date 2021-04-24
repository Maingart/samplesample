from django.contrib import admin
from django.urls import include, path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from follow.router import SwitchDetailRouter
from follow.views import FollowViewSet, UserFollowsViewsSet, \
    UserFollowedViewsSet
from user.views import UserViewSet
from tweet.views import TweetViewSet, UserTweetsViewSet, FeedViewSet

switch_router = SwitchDetailRouter()
router = ExtendedDefaultRouter()

user_route = router.register(r'users', UserViewSet)

user_route.register('tweets', UserTweetsViewSet, 'user-tweets', ['username'])
user_route.register('follows', UserFollowsViewsSet, 'user-follows',
                    ['username'])
user_route.register('followed', UserFollowedViewsSet, 'user-followed',
                    ['username'])

router.register(r'tweets', TweetViewSet)
router.register(r'feed', FeedViewSet)

switch_router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(switch_router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')
         ),
    path('admin/', admin.site.urls)
]
