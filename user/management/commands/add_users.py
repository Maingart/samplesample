from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n: int = options['n']

        last_i = User.objects.last().id
        for i in range(1, options['n'] + 1):
            user = User.objects.get_or_create(username=f'User {last_i + i}')

        self.stdout.write(self.style.SUCCESS('Successfully add %s users' % n))
