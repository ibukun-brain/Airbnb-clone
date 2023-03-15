import auto_prefetch

from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _
from airbnb.utils.models import TimeBasedModel


class Review(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    room = auto_prefetch.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    accuracy = models.PositiveSmallIntegerField(default=0)
    communication = models.PositiveSmallIntegerField(default=0)
    cleanliness = models.PositiveSmallIntegerField(default=0)
    location = models.PositiveSmallIntegerField(default=0)
    check_in = models.PositiveSmallIntegerField(_('Check In'), default=0)
    value = models.PositiveSmallIntegerField(default=0)

    @property
    def preview(self):
        return truncatechars(self.comment, 50)

    def __str__(self):
        return f"{self.user}'s review on {self.room}"
