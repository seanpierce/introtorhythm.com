# Generated by Django 3.1.14 on 2022-11-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0015_liverecording_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liverecording',
            name='show_recording',
            field=models.FileField(blank=True, max_length=500, upload_to='live-recordings/audio'),
        ),
    ]