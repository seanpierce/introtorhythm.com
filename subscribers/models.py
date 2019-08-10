import uuid

from django.db import models

class Subscriber(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)

    class Meta:
        ordering = ['email', ]

    def __str__(self):
        return self.email


class SubscriptionRequest(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)
    token = models.CharField(max_length=100, blank=True,
                            unique=True, default=uuid.uuid4)

    class Meta:
        ordering = ['email', ]

    def __str__(self):
        return self.email
