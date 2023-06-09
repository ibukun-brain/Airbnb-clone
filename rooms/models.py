import auto_prefetch

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from ckeditor.fields import RichTextField

from airbnb.utils.media import MediaHelper
from airbnb.utils.models import NamedTimeBasedModel, TimeBasedModel


class Room(NamedTimeBasedModel):
    host = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    description = RichTextField(_('description'))
    country = CountryField(blank_label=_("(select country)"))
    city = models.CharField(_('city'), max_length=50)
    price = models.PositiveSmallIntegerField(_('price'), default=0)
    address = models.CharField(_('address'), max_length=100)
    baths = models.PositiveSmallIntegerField(_('baths'), default=0)
    beds = models.PositiveSmallIntegerField(_('beds'), default=0)
    bedrooms = models.PositiveSmallIntegerField(_('bedrooms'), default=0)
    guests = models.PositiveSmallIntegerField(_('guests'), default=0)
    check_in = models.TimeField(_('check_in'))
    check_out = models.TimeField(_('checkout'))
    instant_book = models.BooleanField(_('instant book'), default=False)
    room_type = auto_prefetch.ForeignKey(
        'RoomType',
        verbose_name=_('room type'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='rooms'
    )
    amenities = models.ManyToManyField(
        'Amenity',
        blank=True,
        related_name='rooms'
    )
    facilities = models.ManyToManyField(
        'facility',
        blank=True,
        related_name='rooms'
    )
    house_rules = models.ManyToManyField(
        'HouseRule',
        blank=True,
        related_name='rooms'
    )

    @property
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if all_reviews.count() > 0:
            for review in all_reviews:
                all_ratings += review.rating_average

            return all_ratings / len(all_reviews)
        return 0

    def save(self, *args, **kwargs):
        self.city = self.city.capitalize()
        return super().save(*args, **kwargs)


class RoomPhoto(TimeBasedModel):
    room = auto_prefetch.ForeignKey(
        'Room',
        verbose_name=_('room'),
        on_delete=models.CASCADE,
        related_name="roomphotos"
    )
    caption = models.CharField(_('caption'), max_length=100, blank=True)
    image = models.ImageField(
        upload_to=MediaHelper.room_photo_upload_path,
     )

    class Meta:
        verbose_name = 'Room Photo'

    def __str__(self):
        return self.caption


class RoomType(NamedTimeBasedModel):
    subtitle = models.CharField(_('subtitle'), max_length=120, blank=True)

    class Meta:
        verbose_name = 'Room Type'


class Amenity(NamedTimeBasedModel):
    subtitle = models.CharField(_('subtitle'), max_length=120, blank=True)

    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(NamedTimeBasedModel):
    subtitle = models.CharField(_('subtitle'), max_length=120, blank=True)

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(NamedTimeBasedModel):
    subtitle = models.CharField(_('subtitle'), max_length=120, blank=True)

    class Meta:
        verbose_name = 'House Rule'
