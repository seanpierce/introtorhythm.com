import os
import boto3

from django.conf import settings
from django.db import models
from django.dispatch import receiver

from ckeditor.fields import RichTextField

def get_default_title_for_image():
    from datetime import datetime
    now = datetime.now()
    return 'img-%s' % now.strftime("%m%d%Y-%H:%M:%S")


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    info = RichTextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Content"

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default=get_default_title_for_image())
    image = models.ImageField(upload_to='content/images')

    @property
    def filename(self):
        return os.path.basename(self.image.name)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.filename


@receiver(models.signals.post_delete, sender=Image)
def remove_file_from_s3(sender, instance, using, **kwargs):
    """
    Deletes image from filesystem (AWS S3)
    when corresponding `Image` record is deleted.
    """
    instance.image.delete(save=False)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem (AWS S3)
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)