# Generated by Django 4.1.7 on 2023-03-14 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_customuser_options_remove_customuser_birthdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='langauge',
            new_name='language',
        ),
    ]
