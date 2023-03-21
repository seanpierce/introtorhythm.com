from django.db import models


class CallInNumber(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True, help_text='10-digit phone number used for call-in shows. No parentesis, or hyphens - just numbers.')
    active = models.BooleanField(default=True, help_text='Indicates whether or not the call-in number is active')

    class Meta:
        verbose_name_plural = "Call In Number"

    def __str__(self):
        return 'Call In Number'