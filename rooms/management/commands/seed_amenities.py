from django.core.management.base import BaseCommand

from rooms.models import Amenity

NAME = 'Amenity'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def handle(self, *args, **options):
        amenities = [
            'Air conditioning', 'Alarm Clock', 'Balcony',
            'Bathroom', 'Bathtub', 'Bed Linen',
            'Boating', 'Cable TV', 'Carbon monoxide detectors',
            'Chairs', 'Children Area', 'Coffee Maker in Room',
            'Cooking hob', 'Cookware & Kitchen Utensils',
            'Dishwasher', 'Double bed', 'En suite bathroom',
            'Free Parking', 'Free Wireless Internet', 'Freezer',
            'Fridge / Freezer', 'Golf', 'Hair Dryer', 'Heating',
            'Hot tub', 'Indoor Pool', 'Ironing Board',
            'Microwave', 'Outdoor Pool', 'Outdoor Tennis',
            'Oven', 'Queen size bed', 'Restaurant',
            'Shopping Mall', 'Shower', 'Smoke detectors',
            'Sofa', 'Stereo', 'Swimming pool',
            'Toilet', 'Towels', 'TV'
        ]
        for a in amenities:
            _dkaamenity, _ = Amenity.objects.get_or_create(
                name=a
            )
        self.stdout.write(self.style.SUCCESS(f'{NAME} was created'))
