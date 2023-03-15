from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'preview', 'created_at', 'updated_at']
    list_select_related = ['user', 'room']
    autocomplete_fields = ['user', 'room']
    search_fields = ['user__username', 'user__email', 'room_name']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
