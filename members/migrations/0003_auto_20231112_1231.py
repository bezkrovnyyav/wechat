# Generated by Django 3.2.22 on 2023-11-12 10:31

from django.db import migrations


def add_members(apps, schema_editor):
    # We can't import Members model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Member = apps.get_model("members", "Members")
    Member.objects.get_or_create(username='User1') 
    Member.objects.get_or_create(username='User2') 
    Member.objects.get_or_create(username='User3')


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_members_options_alter_members_managers_and_more'),
    ]

    operations = [
        migrations.RunPython(add_members),
    ]
