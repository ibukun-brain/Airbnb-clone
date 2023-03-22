from django.core.management.base import BaseCommand

from home.models import CustomUser

NAME = 'Facility'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def handle(self, *args, **options):
        facilities = [
            'Private entrance', 'Paid parking on premises', 'Gym',
            'Paid parking off premises', 'Elevator', 'Parking'
        ]
        for f in facilities:
            _facility, _ = CustomUser.objects.get_or_create(
                name=f
            )
        self.stdout.write(self.style.SUCCESS(f'{NAME} was created'))
