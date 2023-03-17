import auto_prefetch

from django.db import models
from django.template.defaultfilters import truncatechars, date

from airbnb.utils.models import TimeBasedModel


class Chat(TimeBasedModel):
    participants = models.ManyToManyField(
        "home.CustomUser",
        blank=True,
    )

    @property
    def display_created_date(self):
        return date(self.created_at)

    @property
    def all_participants(self):
        usernames = [user.username for user in self.participants.all()]

        return ', '.join(usernames)

    @property
    def count_messages(self):
        return self.messages.count()

    @property
    def count_participants(self):
        return self.participants.count()

    def __str__(self):
        return f'{self.all_participants} - {self.display_created_date}'


class Message(TimeBasedModel):
    content = models.TextField()
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    chats = auto_prefetch.ForeignKey(
        "Chat",
        on_delete=models.CASCADE,
        related_name='messages'
    )

    @property
    def chat_preview(self):
        return truncatechars(self.content, 50)

    def __str__(self):
        return f'{self.user} says: {self.content}'
