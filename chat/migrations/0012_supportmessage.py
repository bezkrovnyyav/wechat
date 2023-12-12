# Generated by Django 4.2.7 on 2023-12-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20231112_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='User', max_length=255)),
                ('author_email', models.EmailField(max_length=50)),
                ('timecreate', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
