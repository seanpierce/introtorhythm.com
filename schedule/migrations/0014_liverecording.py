# Generated by Django 3.1.14 on 2022-11-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_auto_20221116_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveRecording',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('info', models.TextField(blank=True, default=None, null=True)),
                ('start_date_time', models.DateTimeField(null=True)),
                ('show_image', models.ImageField(blank=True, max_length=500, upload_to='live-recordins/images/')),
                ('show_recording', models.FileField(upload_to='live-recordings/audio')),
            ],
            options={
                'ordering': ['start_date_time'],
            },
        ),
    ]