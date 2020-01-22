# Generated by Django 2.2.4 on 2020-01-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0003_episode_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='tags',
            field=models.CharField(default='', help_text='comma separated. ex: "funk, house, soca disco"', max_length=255),
        ),
    ]