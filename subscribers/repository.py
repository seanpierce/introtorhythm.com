import datetime

from django.db import IntegrityError

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
        except Exception as e:
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
            If a Subscriber is already in the database with the email address provided,
            returns false. Otherwise returns true.
        """

        try:
            Subscriber.objects.create(email=email)
            return True
        except Exception as e:
            return False

    def remove_subscription_request(token):
        """Deletes a SubscriptionRequest record from the database when 
        provided a token.
        
        Args: 
            token: a string representing a token for a SubscriptionRequest obejct.

        Returns:
            void
        """
        SubscriptionRequest.objects.get(token=token).delete()

    def create_subscription_request(email):
        """Creates a new SubscriptionRequest record.

        Args:
            email: a string representing anemail address for the subscripton request.

        Returns:
            If a SubscriptionRequest is already in the database with the email address provided,
            returns false. Otherwise returns true.
        """
        try:
            SubscriptionRequest.objects.create(email=email)
            return True
        except Exception as e:
            return False

    def get_token_by_email(email):
            token = SubscriptionRequest.objects.get(email=email)
            return token.token
