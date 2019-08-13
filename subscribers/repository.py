import datetime

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber, SubscriptionRequest

class SubscriberRepository(object):
    """Access layer for Subscriber and SubscriptionRequest data."""

    def get_request_by_token(token):
        """Finds and returns a dict representing a SubscriptionRequest
        which matchs the given token.

        Args:
            token: a string representing a token for a subscription request.

        Returns:
            If a token with matches the provided token is present on a 
            SubscriptionRequest object in the database, the method returns 
            a dict containiing the created_at, email, and token fields.
            Retruns None If no token matches are found in the database.
        """

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
        """Creates a new Subscriber in the database when provided an email address.

        Args:
            email: an email address to be assigned to the newly created Subscriber.

        Returns:
            If a SUbscriber is already in the database with the email address provided,
            returns false. Otherwise returns true.
        """

        try:
            Subscriber.objects.create(email=email)
            return True
        except IntegrityError:
            return False

    def remove_subscription_request(token):
        """Deletes a SubscriptionRequest record from the database when 
        provided a token.
        
        Args: 
            token: a string representing a token for a SubscriptionRequest obejct.

        Returns:
            void
        """
        SubscriptionRequest.objects.filter(token=token).delete()