import boto3
import datetime
import io
import os
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from PIL import Image


class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=3)
    content = RichTextField()
    tags = models.CharField(max_length=255, default='', blank=True, null=True, help_text='Comma separated. ex: "funk, house, soca disco".')
    image = models.ImageField(upload_to = 'episodes/images/', max_length = 500, default = None, help_text='Used as the background image for the episode.')
    audio = models.FileField(upload_to = 'episodes/audio/', max_length = 500, default = None)
    active = models.BooleanField(default=True, help_text='Determines whether or not an episode will be visible on the front-end of the website.')
    featured = models.BooleanField(default=False, help_text='If featured, an episode will persist indefinitely without expiration. Even when featured, the episode must be active to be viewed in the front-end.')
    expiration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-number']

    def __str__(self):
        return '%s- %s' %(self.number, self.title)

    def save(self, *args, **kwargs):
        super(Episode, self).save(*args, **kwargs)
        self.upload_thumbnail()

    def upload_thumbnail(self):
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        filename = 'media/episodes/images/thumbnails/' + os.path.basename(self.image.name)

        image = Image.open(self.image)
        image.thumbnail((100,100), Image.ANTIALIAS)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        buffer = io.BytesIO()
        image.save(buffer, "JPEG")
        buffer.seek(0)
        bucket.put_object(Key=filename, Body=buffer, ACL='public-read')


@receiver(models.signals.pre_save, sender=Episode)
def pre_save(sender, instance, **kwargs):
    """
    Method that is executed before the instance is saved to the database.
    """
    set_expiration(instance)
    auto_delete_image_on_change(instance)
    auto_delete_audio_on_change(instance)


@receiver(models.signals.post_delete, sender=Episode)
def post_delete(sender, instance, using, **kwargs):
    """
    Method that is executed after the instance is deleted from the database.
    """
    delete_image_when_instance_is_deleted(instance)
    delete_audio_when_instance_is_deleted(instance)


def set_expiration(instance):
    """
    Updates the episode's expiration date based on its active and featured properties.
    """    
    is_featured = instance.featured
    is_active = instance.active

    if is_active and not is_featured:
        instance.expiration_date = datetime.datetime.now() + datetime.timedelta(days = 60)
    else:
        instance.expiration_date = None


def auto_delete_image_on_change(instance):
    """
    Deletes old image from filesystem (AWS S3)
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return None

    try:
        old_file = Episode.objects.get(pk=instance.pk).image
    except:
        return None

    new_file = instance.image

    if not old_file == new_file:
        old_file.delete(save=False)


def auto_delete_audio_on_change(instance):
    """
    Deletes old audio from filesystem (AWS S3)
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return None

    try:
        old_file = Episode.objects.get(pk=instance.pk).audio
    except:
        return None

    new_file = instance.audio

    if not old_file == new_file:
        old_file.delete(save=False)


def delete_image_when_instance_is_deleted(instance):
    """
    Deletes image from filesystem (AWS S3)
    when corresponding `Image` record is deleted.
    """
    instance.image.delete(save=False)


def delete_audio_when_instance_is_deleted(instance):
    """
    Deletes audio from filesystem (AWS S3)
    when corresponding `Image` record is deleted.
    """
    instance.audio.delete(save=False)

        
