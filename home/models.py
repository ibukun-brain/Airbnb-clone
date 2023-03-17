import auto_prefetch

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from airbnb.utils.media import MediaHelper
from airbnb.utils.choices import (
    Currency, Gender,
    Language,
)
from airbnb.utils.models import TimeBasedModel


class CustomUser(TimeBasedModel, AbstractUser):
    """
        Custom User Model
    """
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    email = models.EmailField(_("email address"), unique=True)
    gender = models.CharField(
        _("gender"),
        choices=Gender.choices,
        default=_(Gender.Male),
        max_length=20
    )
    # mobile_no = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(
        _("avatar"),
        upload_to=MediaHelper.avatar_upload_path,
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(_("date of birth"), null=True)
    language = models.CharField(
        _("langauge"),
        choices=Language.choices,
        default=_(Language.English),
        max_length=2
    )
    currency = models.CharField(
        _("currency"),
        max_length=3,
        choices=Currency.choices,
        default=_(Currency.USD)
    )
    bio = models.TextField(_("bio"), blank=True)
    superhost = models.BooleanField(default=False)
    objects = UserManager()

    class Meta(auto_prefetch.Model.Meta):
        ordering = ["first_name", "last_name"]
        verbose_name = "user"
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def image_url(self):
        """return image if it exists otherwise use a default"""
        if self.avatar:
            return self.avatar.url

        return f"{settings.STATIC_URL}images/avatar/placeholder.jpg"
