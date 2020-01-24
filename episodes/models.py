import os
import io
import boto3

from django.conf import settings
from django.db import models

from ckeditor.fields import RichTextField
from PIL import Image

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=3)
    content = RichTextField()
    tags = models.CharField(max_length=255, default='', help_text='comma separated. ex: "funk, house, soca disco"')
    image = models.ImageField(upload_to='episodes/images/',
        max_length=500, default='assets/not-found.jpg')
    audio = models.FileField(upload_to='episodes/audio/',
        max_length=500, default='assets/not-found.mp3')
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-number',]

    def __str__(self):
        return self.number + '- ' + self.title

    def save(self, *args, **kwargs):
        super(Episode, self).save(*args, **kwargs)
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        filename = 'media/episodes/images/thumbnails/' + os.path.basename(self.image.name)
        image = Image.open(self.image)
        image.thumbnail((100,100), Image.ANTIALIAS)
        buffer = io.BytesIO()
        image.save(buffer, "JPEG")
        buffer.seek(0)
        bucket.put_object(Key=filename, Body=buffer, ACL='public-read')
        
