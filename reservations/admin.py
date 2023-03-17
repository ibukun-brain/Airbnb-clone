from django.contrib import admin
from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'room', 'guest', 'status',
        'check_in', 'check_out', 'in_progess',
        'is_finished'
    ]
    date_hierarchy = 'check_in'
    search_fields = ['room__name', 'guest__username', 'guest__email']
    list_select_related = ['room', 'guest']
    autocomplete_fields = ['room', 'guest']
    list_filter = [
        'status', 'check_in', 'check_out',
        'created_at', 'updated_at'

    ]
