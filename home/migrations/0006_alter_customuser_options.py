# Generated by Django 4.1.7 on 2023-03-16 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_langauge_customuser_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'base_manager_name': 'prefetch_manager', 'ordering': ['first_name', 'last_name'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]