import admin_thumbnails

from django.contrib import admin
from rooms.models import (
    Amenity, Facility, HouseRule,
    Room, RoomPhoto, RoomType
)


@admin.register(RoomPhoto)
@admin_thumbnails.thumbnail('image', background=True)
class RoomAdminPhoto(admin.ModelAdmin):
    search_fields = ['room__name', 'caption']
    date_hierarchy = 'created_at'
    list_filter = ['created_at', 'updated_at']
    list_select_related = ['room']
    autocomplete_fields = ['room']
    list_display = ['image_thumbnail', 'caption', 'created_at', 'updated_at']


@admin_thumbnails.thumbnail('image')
class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            'Basic Info',
            {'fields': (
                'name', 'description', 'country',
                'city', 'address', 'price'
                )}
        ),
        (
            'Time',
            {'fields': ('check_in', 'check_out', 'instant_book')}
        ),
        (
            'Spaces',
            {'fields': ('baths', 'beds', 'bedrooms', 'guests')}
        ),
        (
            'More About The Space',
            {'fields': ('amenities', 'facilities', 'house_rules')}
        ),
        (
            'Last Details',
            {'fields': ('host',)}
        ),
    )

    list_display = [
        'name', 'host', 'country',
        'city', 'address', 'instant_book',
        'price', 'count_amenities', 'count_photos',
        'total_rating'
    ]
    ordering = ['name', 'price', 'bedrooms']
    date_hierarchy = 'created_at'
    list_filter = [
        'created_at', 'updated_at', 'instant_book',
        'baths', 'beds', 'bedrooms',
        'guests',
    ]
    search_fields = ['host__username', 'host_email', 'name', 'description']
    list_select_related = ['host', 'room_type']
    autocomplete_fields = ['host', 'room_type']
    filter_horizontal = ['amenities', 'facilities', 'house_rules']
    inlines = [RoomPhotoInline]

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = 'amenities count'

    def count_photos(self, obj):
        return obj.roomphotos.count()

    # def save_model(self, request, obj, form, change):
    #     obj.city = obj.city.capitalize()
    #     return super().save_model(request, obj, form, change)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'used_by', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'subtitle']
    list_filter = ['created_at', 'updated_at']

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'subtitle']
    list_filter = ['created_at', 'updated_at']


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'subtitle']
    list_filter = ['created_at', 'updated_at']


@admin.register(HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'subtitle']
    list_filter = ['created_at', 'updated_at']
