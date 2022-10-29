from django.db import models

from ckeditor.fields import RichTextField


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    info = RichTextField(null=True, blank=True)
    plain_text = models.CharField(max_length=500, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Content"

    def __str__(self):
        return self.name