from django.db import models

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=3)
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    audio = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.number + '- ' + self.title