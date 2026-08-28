from django.db import models


class Connections(models.Model):
    id = models.AutoField(primary_key=True)
    connection_url = models.CharField(max_length=500, null=True, blank=True, help_text='URL that the UI will connect to to play the stream.')
    call_in_number = models.CharField(max_length=10, null=True, blank=True, help_text='Number for the call-in line. Enter number with no special characters. ex: 5036103801')

    class Meta:
        verbose_name_plural = "Connections"

    def __str__(self):
        return 'Connections'