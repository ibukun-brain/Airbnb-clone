# Generated by Django 4.1.7 on 2023-03-16 08:25

import airbnb.utils.media
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0014_alter_roomphoto_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomphoto',
            name='image',
            field=models.ImageField(upload_to=airbnb.utils.media.MediaHelper.room_photo_upload_path),
        ),
    ]
