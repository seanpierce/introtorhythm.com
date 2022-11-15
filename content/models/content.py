import os
from ckeditor.fields import RichTextField
from django.db import models
from django.dispatch import receiver


class BackgroundImage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='content/images')
    active = models.BooleanField(default=False)

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
    except BackgroundImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(save=False)


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    info = RichTextField(null=True, blank=True)
    plain_text = models.CharField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Content"

    def __str__(self):
        return self.name


class SiteInfo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    info = RichTextField(null=True, blank=True, help_text='Content that will be displayed in the info section of the website')

    class Meta:
        verbose_name_plural = 'Info / About'

    def __str__(self):
        return 'Info / About'


class LiveCallout(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500, null=True, blank=True, help_text='Content that is populated in the marquee')
    active = models.BooleanField(default=True, help_text='Indicates whether or not the content will show on the marquee')

    class Meta:
        verbose_name_plural = "Live Callout"

    def __str__(self):
        return 'Live Callout'