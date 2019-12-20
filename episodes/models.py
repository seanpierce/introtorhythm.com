from django.db import models

from ckeditor.fields import RichTextField

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=3)
    content = RichTextField()
    image = models.ImageField(upload_to='episodes/images/',
        max_length=500, default='assets/not-found.jpg')
    audio = models.FileField(upload_to='episodes/audio/',
        max_length=500, default='assets/not-found.mp3')
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-number',]

    def __str__(self):
        return self.number + '- ' + self.title
