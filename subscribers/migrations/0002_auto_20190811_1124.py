# Generated by Django 2.2.4 on 2019-08-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subscriptionrequest',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]