import auto_prefetch

from django.db import models

from airbnb.utils.models import NamedTimeBasedModel


class List(NamedTimeBasedModel):
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField(
        'rooms.Room',
        blank=True
    )

    def count_rooms(self):
        return self.rooms.count()
    count_rooms.short_description = 'Number of rooms'

    def __str__(self):
        return self.name
