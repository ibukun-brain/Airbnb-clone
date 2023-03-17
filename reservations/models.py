import auto_prefetch

from django.db import models
from django.utils import timezone

from airbnb.utils.models import TimeBasedModel
from airbnb.utils.choices import ReservationStatus


class Reservation(TimeBasedModel):
    status = models.CharField(
        choices=ReservationStatus.choices,
        max_length=12,
        default=ReservationStatus.Pending
    )
    guest = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    room = auto_prefetch.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progess(self):
        now = timezone.now().date()
        return self.check_in <= now < self.check_out

    in_progess.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
