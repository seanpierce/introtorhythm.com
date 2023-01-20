import pytz
from datetime import datetime, timedelta
from django.db import models
from django.dispatch import receiver
from schedule.helpers import TIMES, DURATION


class Show(models.Model):
    """
    Django model for the shows.show ORM/ data table.
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.TextField(default=None, blank=True, null=True)
    date = models.DateField()
    start_time = models.IntegerField(choices=TIMES)
    duration = models.IntegerField(choices=DURATION, default=1)
    start_date_time = models.DateTimeField(null=True)
    end_date_time = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    show_image = models.ImageField(upload_to='shows/images/', max_length=500, blank=True, help_text='The show\'s image that will be displayed on the site while the show is live.')
    show_flyer = models.ImageField(upload_to='shows/images/', max_length=500, blank=True, help_text='The show\'s flyer that will be used on the schedule page and for social media.')

    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ['date', 'start_time']

    def __str__(self):
        return self.title


@receiver(models.signals.pre_save, sender=Show)
def pre_save(sender, instance, **kwargs):
    """
    Method that is executed before the instance is saved to the database.
    """
    set_end_date_time(instance)
    auto_delete_files_on_change(instance)


@receiver(models.signals.post_delete, sender=Show)
def post_delete(sender, instance, using, **kwargs):
    """
    Method that is executed after the instance is deleted from the database.
    """
    delete_files_when_instance_is_deleted(instance)


def set_end_date_time(instance):
    """
    Programatically sets the end date time field 
    based on the start time and the duration.
    """
    start_date_time = datetime(
        day=instance.date.day,
        month=instance.date.month,
        year=instance.date.year,
        hour=instance.start_time
    )

    instance.start_date_time = pytz.utc.localize(start_date_time) 
    instance.end_date_time = instance.start_date_time + timedelta(hours=instance.duration)


def auto_delete_files_on_change(instance):
    """
    Deletes old image(s) from filesystem (AWS S3)
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return None

    try:
        old_image = Show.objects.get(pk=instance.pk).show_image
        old_flyer = Show.objects.get(pk=instance.pk).show_flyer
    except:
        return None

    new_image = instance.show_image
    new_flyer = instance.show_flyer

    if not old_image == new_image:
        old_image.delete(save=False)

    if not old_flyer == new_flyer:
        old_flyer.delete(save=False)


def delete_files_when_instance_is_deleted(instance):
    """
    Deletes image(s) from filesystem (AWS S3)
    when corresponding `Image` record is deleted.
    """
    instance.show_image.delete(save=False)
    instance.show_flyer.delete(save=False)