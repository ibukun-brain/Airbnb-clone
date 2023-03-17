from django.contrib import admin
from chats.models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [
        'all_participants', 'created_at',
        'count_messages', 'count_participants'
    ]
    list_filter = ['created_at', 'updated_at']
    filter_horizontal = ['participants']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'chat_preview', 'created_at', 'updated_at']
    autocomplete_fields = ['user']
    list_select_related = ['user']
    search_fields = ['user__username', 'user__email', 'content']
    date_hierarchy = 'created_at'
