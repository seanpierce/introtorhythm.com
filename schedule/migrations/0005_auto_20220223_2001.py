# Generated by Django 3.1.14 on 2022-02-24 04:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20220216_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='pre_record_audio',
            field=models.FileField(blank=True, max_length=500, storage=django.core.files.storage.FileSystemStorage(location='uploads/scheduled/'), upload_to=''),
        ),
    ]