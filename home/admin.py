from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from home.models import CustomUser

admin.site.site_header = "Airbnb Administration"
admin.site.site_title = "Airbnb"
admin.site.index_title = "Airbnb"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "gender",
                    "bio",
                    "avatar",
                    "date_of_birth",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "password1", "password2"), },), )

    def thumbnail(self, object):
        img = object.image_url
        return format_html('<img src="{0}" width="30"/>', img)

    thumbnail.short_description = 'Avatar'
    list_display = [
        "thumbnail",
        "first_name",
        "last_name",
        "email",
        "gender",
        "superhost",
        "is_staff",
        "is_superuser",
    ]
    ordering = ("first_name", "last_name")
    list_display_links = ["first_name", "email"]
    list_filter = [
        "currency",
        "language",
        "created_at",
        "superhost",
        "is_staff",
        "is_superuser",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "username",
    ]
    date_hierarchy = "date_joined"
