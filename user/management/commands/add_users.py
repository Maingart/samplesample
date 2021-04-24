from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        n: int = options['n']

        for i in range(options['n']):
            user = User.objects.create(username=f'User {i}')
            user.save()

        self.stdout.write(self.style.SUCCESS('Successfully add %s users' %
                                             n))
