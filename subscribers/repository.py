import datetime

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber, SubscriptionRequest

class SubscriberRepository(object):
    """Access layer for Subscriber and SubscriptionRequest data."""

    @staticmethod
    def get_request_by_token(token):
        """Finds and returns a dict representing a SubscriptionRequest
        which matchs the given token.

        Args:
            token: a string representing a token for a subscription request.

        Returns:
            If a token with matches the provided token is present on a
            SubscriptionRequest object in the database, the method returns
            a dict containing the created_at, email, and token fields.
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

    @staticmethod
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

    @staticmethod
    def remove_subscription_request(token):
        """Deletes a SubscriptionRequest record from the database when
        provided a token.

        Args:
            token: a string representing a token for a SubscriptionRequest object.

        Returns:
            void
        """
        SubscriptionRequest.objects.get(token=token).delete()

    @staticmethod
    def create_subscription_request(email, ipAddress):
        """Creates a new SubscriptionRequest record.

        Args:
            email: a string representing anemail address for the subscripton request.

        Returns:
            If a SubscriptionRequest is already in the database with the email address provided,
            returns false. Otherwise returns true.
        """
        try:
            SubscriptionRequest.objects.create(email=email, ip_address=ipAddress)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_token_by_email(email):
        """Returns a string representing a token found in the SubscriptionRequest table.

        Args:
            email: a string representing an email for a SubscriptionRequest object.

        Returns:
            The token as a string for a given SubscriptionRequest object
            matching the provided email address. If no SubscriptionRequest is found,
            returns None.
        """
        try:
            token = SubscriptionRequest.objects.get(email=email)
            return token.token
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def unsubscribe(email):
        try:
            subscriber = Subscriber.objects.get(email=email).delete()
            return True
        except ObjectDoesNotExist:
            return False
