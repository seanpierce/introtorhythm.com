from ckeditor.fields import RichTextField
from django.db import models


class SiteInfo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    info = RichTextField(null=True, blank=True, help_text='Content that will be displayed in the info section of the website')

    class Meta:
        verbose_name_plural = 'Info / About'

    def __str__(self):
        return 'Info / About'