# Generated by Django 3.1.14 on 2022-10-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20221027_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_image',
            field=models.ImageField(blank=True, default='assets/not-found.jpg', max_length=500, upload_to='shows/images/'),
        ),
    ]