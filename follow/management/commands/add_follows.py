from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from follow.models import Follow


class Command(BaseCommand):
    help = 'Create follows'

    def handle(self, *args, **options):
        users = User.objects.all()

        follower = users[0]
        for user in users[1:]:
            Follow.objects.create(follower=follower, follows=user)
            follower = user

        self.stdout.write(self.style.SUCCESS('Successfully follows'))
