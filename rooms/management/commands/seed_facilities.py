from django.core.management.base import BaseCommand

from home.models import CustomUser

NAME = 'Facility'


class Command(BaseCommand):

    help = f'This command creates a test data for a {NAME} model'

    def add_arguments(self, parser):
        return super().add_arguments(
            '--number',
            type=int,
            default=1,
            help=f'How many {NAME} do you want to create'
        )

    def handle(self, *args, **options):
        facilities = [
            'Private entrance', 'Paid parking on premises', 'Gym',
            'Paid parking off premises', 'Elevator', 'Parking'
        ]
        for f in facilities:
            facility, created = CustomUser.objects.get_or_create(
                name=f
            )
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} was created'))
