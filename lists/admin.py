from django.contrib import admin
from lists.models import List

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_select_related = ['user']
    autocomplete_fields = ['user']
    search_fields = ['name', 'user__username', 'user__email', 'rooms__name']
    list_display = ['name', 'user', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_filter = ['created_at', 'updated_at']
    filter_horizontal = ['rooms']
