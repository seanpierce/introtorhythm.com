# Generated by Django 3.1.14 on 2022-10-27 16:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_show_show_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_image',
            field=models.ImageField(blank=True, max_length=500, storage=django.core.files.storage.FileSystemStorage(location='uploads/scheduler/'), upload_to=''),
        ),
    ]
