# Generated by Django 4.1.7 on 2023-03-16 13:55

import auto_prefetch
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0015_alter_roomphoto_image'),
        ('reviews', '0002_alter_review_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='room',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='rooms.room'),
        ),
    ]
