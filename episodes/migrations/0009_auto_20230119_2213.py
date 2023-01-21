# Generated by Django 3.1.14 on 2023-01-20 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0008_auto_20230119_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 18, 22, 13, 7, 488167), null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='tags',
            field=models.CharField(blank=True, default='', help_text='comma separated. ex: "funk, house, soca disco"', max_length=255, null=True),
        ),
    ]