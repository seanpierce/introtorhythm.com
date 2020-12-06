import os
from django.db import models
from ckeditor.fields import RichTextField


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