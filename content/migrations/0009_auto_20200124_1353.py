# Generated by Django 2.2.4 on 2020-01-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20200124_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='img-01242020-13:53:02', max_length=50),
        ),
    ]
