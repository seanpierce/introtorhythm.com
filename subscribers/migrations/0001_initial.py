# Generated by Django 2.2.4 on 2019-12-07 21:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='SubscriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('token', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]