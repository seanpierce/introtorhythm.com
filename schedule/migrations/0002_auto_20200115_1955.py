# Generated by Django 2.2.4 on 2020-01-16 03:55

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='audio',
            field=models.FileField(blank=True, max_length=500, storage=django.core.files.storage.FileSystemStorage(location='uploads/'), upload_to=''),
        ),
    ]