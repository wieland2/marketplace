# Generated by Django 4.2.6 on 2025-03-09 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profiles_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='emails',
            new_name='email',
        ),
    ]
