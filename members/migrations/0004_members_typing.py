# Generated by Django 4.2.7 on 2023-11-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20231112_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='typing',
            field=models.BooleanField(default=False),
        ),
    ]
