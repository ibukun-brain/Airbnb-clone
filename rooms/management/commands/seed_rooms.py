import random

from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand

from django_seed import Seed

from home.models import CustomUser
from rooms.models import (
    Room, RoomPhoto, RoomType,
    Amenity, HouseRule, Facility
)

NAME = 'Room'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=1,
            help=f'How many {NAME} do you want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        all_users = CustomUser.objects.all()
        room_types = RoomType.objects.all()
        seeder.add_entity(Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            'beds': lambda x: random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'baths': lambda x: random.randint(1, 5),
            'guests': lambda x: random.randint(1, 20),
            'price': lambda x: random.randint(1, 300),
        })
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        house_rules = HouseRule.objects.all()
        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for _ in range(3, random.randint(10, 30)):
                _photo, _ = RoomPhoto.objects.get_or_create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    image=f'room_photos/{random.randint(1, 31)}.jpg'
                )
            for amenity in amenities:
                rand_int = random.randint(0, 15)
                if rand_int % 2 < 1:
                    room.amenities.add(amenity)

            for facility in facilities:
                rand_int = random.randint(0, 15)
                if rand_int % 2 < 1:
                    room.facilities.add(facility)

            for house_rule in house_rules:
                rand_int = random.randint(0, 15)
                if rand_int % 2 < 1:
                    room.house_rules.add(house_rule)

        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} was created'))
