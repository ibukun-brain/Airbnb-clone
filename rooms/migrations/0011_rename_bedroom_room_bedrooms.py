# Generated by Django 4.1.7 on 2023-03-16 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_alter_roomphoto_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bedroom',
            new_name='bedrooms',
        ),
    ]
