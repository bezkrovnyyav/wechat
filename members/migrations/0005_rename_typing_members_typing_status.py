# Generated by Django 4.2.7 on 2023-11-26 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_members_typing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='typing',
            new_name='typing_status',
        ),
    ]
