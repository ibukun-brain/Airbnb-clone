import random

from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

from django_seed import Seed

from home.models import CustomUser
from lists.models import List
from rooms.models import Room

NAME = 'List'


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

        seeder.add_entity(List, number, {
            'user': lambda x: random.choice(users),
        })
        created_lists = seeder.execute()
        created_clean = flatten(list(created_lists.values()))
        for pk in created_clean:
            list_obj = List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5):random.randint(6, 30)]
            list_obj.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f'{number} {NAME}s was created'))
