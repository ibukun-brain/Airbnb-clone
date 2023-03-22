import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from django_seed import Seed

from home.models import CustomUser
from reservations.models import Reservation
from rooms.models import Room


NAME = 'reservation'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=1,
            help=f'How many {NAME} do u want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = CustomUser.objects.all()
        rooms = Room.objects.all()

        seeder.add_entity(Reservation, number, {
            'status': lambda x: random.choice([
                'pending', 'confirmed', 'canceled'
                ]),
            'guest': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'check_in': lambda x: datetime.now(),
            'check_out': (
                lambda x: datetime.now()+timedelta(days=random.randint(23, 31))
            )
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} was created'))
