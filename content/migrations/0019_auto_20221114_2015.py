# Generated by Django 3.1.14 on 2022-11-15 04:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_auto_20221114_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('info', ckeditor.fields.RichTextField(blank=True, help_text='Content that will be displayed in the info section of the website', null=True)),
            ],
            options={
                'verbose_name_plural': 'Info / About',
            },
        ),
        migrations.AlterField(
            model_name='livecallout',
            name='active',
            field=models.BooleanField(default=True, help_text='Indicates whether or not the content will show on the marquee'),
        ),
        migrations.AlterField(
            model_name='livecallout',
            name='content',
            field=models.CharField(blank=True, help_text='Content that is populated in the marquee', max_length=500, null=True),
        ),
    ]