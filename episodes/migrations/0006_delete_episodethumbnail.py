# Generated by Django 2.2.4 on 2020-01-24 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0005_episodethumbnail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EpisodeThumbnail',
        ),
    ]