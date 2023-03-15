# Generated by Django 4.1.7 on 2023-03-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_amenity_facility_houserule_remove_room_room_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='rooms.amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='rooms.facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, to='rooms.houserule'),
        ),
    ]
