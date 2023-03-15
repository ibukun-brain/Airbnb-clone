# Generated by Django 4.1.7 on 2023-03-15 05:37

import auto_prefetch
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0010_alter_roomphoto_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('accuracy', models.PositiveSmallIntegerField(default=0)),
                ('communication', models.PositiveSmallIntegerField(default=0)),
                ('cleanliness', models.PositiveSmallIntegerField(default=0)),
                ('location', models.PositiveSmallIntegerField(default=0)),
                ('check_in', models.PositiveSmallIntegerField(default=0)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('room', auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
                ('user', auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]