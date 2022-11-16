import os
from django.db import models
from django.dispatch import receiver


class BackgroundImage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='content/images', help_text='Image that will show as the background of the "Live" page')
    active = models.BooleanField(default=False, help_text='Toggle used to show or not show the associated image on the "Live" page')

    class Meta:
        verbose_name_plural = "Background Image"

    @property
    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.filename


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
    except:
        return False

    new_file = instance.image

    if not old_file == new_file:
        old_file.delete(save=False)
