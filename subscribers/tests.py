from django.test import TestCase
from django.db import IntegrityError

from .models import Subscriber, SubscriptionRequest
from .repository import SubscriberRepository as repo

class SubscriberTestCase(TestCase):
    def setUp(self):
        # create requests
        SubscriptionRequest.objects.create(email='one@test.com')
        SubscriptionRequest.objects.create(email='two@test.com')
        SubscriptionRequest.objects.create(email='three@test.com')
        # create subscriber
        Subscriber.objects.create(email='four@test.com')
        Subscriber.objects.create(email='five@test.com')

    def test_get_request_by_token(self):
        """Ensures that the repository is able to successfully retrieve a dict
        containing information about the subscription request when supplied a token.
        """
        req = SubscriptionRequest.objects.get(email='one@test.com')
        selected_req = repo.get_request_by_token(req.token)
        self.assertEqual(req.token, selected_req['token'])

    def test_create_subscriber(self):
        """Ensures that the repository is able to successfully
        create a new subscriber in the database when provided an email address.
        """
        repo.create_subscriber('six@test.com')
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 3)

    def test_remove_subscription_request(self):
        """Ensures that the repository is able to successfully
        delete a subscription request from the database when supplied a token."""
        req = SubscriptionRequest.objects.get(email='one@test.com')
        repo.remove_subscription_request(req.token)
        count = SubscriptionRequest.objects.all().count()
        self.assertEqual(count, 2)

    def test_subscriber_model_method_str(self):
        """Ensures that the __str__ class method for the
        Subscriber model successfully returns the expected result."""
        sub = Subscriber.objects.get(email='four@test.com')
        self.assertEqual('four@test.com', sub.__str__())

    def test_subscription_request_model_method_str(self):
        """Ensure that the __str__ method for the 
        SuscriptionRequest model successfully returns the expected result."""
        req = SubscriptionRequest.objects.get(email='one@test.com')
        self.assertEqual('one@test.com', req.__str__())

    def test_subscription_request_email_unique(self):
        """Ensures that the unique constraint is enforces on the
        Email column for the SubscriptionRequest model."""
        try:
            SubscriptionRequest.objects.create(email='one@test.com')
        except IntegrityError:
            pass

    def test_subscriber_email_unique(self):
        """Ensures that the unique constraint is enforces on the
        Email column for the Subscriber model."""
        try:
            Subscriber.objects.create(email='four@test.com')
        except IntegrityError:
            pass