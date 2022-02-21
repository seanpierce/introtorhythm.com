from django.db import models
from django.core.files.storage import FileSystemStorage
from .helpers import TIMES

fs = FileSystemStorage(location='uploads/scheduled/')

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
    active = models.BooleanField(default=True)
    pre_record_audio = models.FileField(storage=fs, max_length=500, blank=True)

    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ['date', 'start_time']

    def __str__(self):
        return self.title
