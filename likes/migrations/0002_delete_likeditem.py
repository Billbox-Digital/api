# Generated by Django 3.2.9 on 2023-01-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikedItem',
        ),
    ]
