import os
import boto3
from django.dispatch import receiver
from django.db import models
from .background_image import BackgroundImage
from .content import Content


@receiver(models.signals.post_delete, sender=BackgroundImage)
def remove_file_from_s3(sender, instance, using, **kwargs):
    """
    Deletes image from filesystem (AWS S3)
    when corresponding `Image` record is deleted.
    """
    instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=BackgroundImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem (AWS S3)
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = BackgroundImage.objects.get(pk=instance.pk).image
    except BackgroundImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)