import pytz
from datetime import datetime, timedelta
from django.db import models
from django.dispatch import receiver
from .helpers import TIMES, DURATION


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
    show_image = models.ImageField(upload_to='shows/images/', max_length=500, blank=True)

    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ['date', 'start_time']

    def __str__(self):
        return self.title


@receiver(models.signals.pre_save, sender=Show)
def auto_delete_file_on_change(sender, instance, **kwargs):
    start_date_time = datetime(
        day=instance.date.day,
        month=instance.date.month,
        year=instance.date.year,
        hour=instance.start_time
    )

    instance.start_date_time = pytz.utc.localize(start_date_time) 
    instance.end_date_time = instance.start_date_time + timedelta(hours=instance.duration)