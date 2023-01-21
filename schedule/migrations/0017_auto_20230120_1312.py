# Generated by Django 3.1.14 on 2023-01-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0016_auto_20221127_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_flyer',
            field=models.ImageField(blank=True, help_text="The show's flyer that will be used on the schedule page and for social media.", max_length=500, upload_to='shows/images/'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_image',
            field=models.ImageField(blank=True, help_text="The show's image that will be displayed on the site while the show is live.", max_length=500, upload_to='shows/images/'),
        ),
    ]