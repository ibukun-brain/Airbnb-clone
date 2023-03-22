from django.core.management.base import BaseCommand

from django_seed import Seed

from home.models import CustomUser

NAME = 'User'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=2,
            help=f'How many {NAME}s do u want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(CustomUser, number, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME}s was created'))
