import datetime

from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber, SubscriptionRequest

class SubscriberRepository(object):

    def get_request_by_token(token):
        try:
            request = SubscriptionRequest.objects.get(token=token)
        except ObjectDoesNotExist:
            return None

        return {
            'created_at': request.created_at,
            'email': request.email,
            'token': request.token
        }

    def create_subscriber(email):
        subscriber, created_new = Subscriber.objects.get_or_create(email=email)
        if created_new:
            return True
        else:
            return False

    def remove_subscription_request(token):
        SubscriptionRequest.objects.filter(token=token).delete()