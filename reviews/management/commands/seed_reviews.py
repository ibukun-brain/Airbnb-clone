import random

from django.core.management.base import BaseCommand

from django_seed import Seed

from home.models import CustomUser
from reviews.models import Review
from rooms.models import Room

NAME = 'Review'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=1,
            help=f'How many {NAME}s do you want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = CustomUser.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(Review, number, {
            'user': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'accuracy': lambda x: random.randint(0, 6),
            'communication': lambda x: random.randint(0, 6),
            'cleanliness': lambda x: random.randint(0, 6),
            'location': lambda x: random.randint(0, 6),
            'check_in': lambda x: random.randint(0, 6),
            'value': lambda x: random.randint(0, 6),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME}s was created'))
