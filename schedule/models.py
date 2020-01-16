from django.db import models
from django.core.files.storage import FileSystemStorage


from .helpers import DAYS, TIMES

fs = FileSystemStorage(location='uploads/')

class Show(models.Model):
    """
    Django model for the shows.show ORM/ data table.
    """
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    start_time = models.IntegerField(choices=TIMES)
    day = models.IntegerField(choices=DAYS)
    active = models.BooleanField(default=True)
    pre_record = models.BooleanField(default=True)
    audio = models.FileField(storage=fs, max_length=500, blank=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return self.title
