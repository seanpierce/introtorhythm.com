import requests, json

from django.apps import apps
from django.test import TestCase, Client
from django.db import IntegrityError
from subscribers.apps import SubscribersConfig

from .models import Subscriber, SubscriptionRequest
from .views import SubscriptionRequestAPI, SubscrptionConfirmationAPI
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
        Email column for the SubscriptionRequest model.
        """
        try:
            SubscriptionRequest.objects.create(email='one@test.com')
        except IntegrityError:
            pass

    def test_subscriber_email_unique(self):
        """Ensures that the unique constraint is enforces on the
        Email column for the Subscriber model.
        """
        try:
            Subscriber.objects.create(email='four@test.com')
        except IntegrityError:
            pass

    def test_create_subscription_request(self):
        """Ensures that a subscription request is successfully created.
        """
        self.assertEqual(repo.create_subscription_request('seven@test.com'), True)

    def test_create_subscription_request_failure(self):
        """Ensures that a subscription request will not be created 
        if the provided email address is not unique.
        """
        self.assertEqual(repo.create_subscription_request('two@test.com'), False)

    def test_get_token_by_email(self):
        """Ensures that the repository is able to fetch a SubscriptionRequest
        token when provided an email address.
        """
        new_token = SubscriptionRequest.objects.create(email='test123@test.com')
        self.assertEqual(str(new_token.token), repo.get_token_by_email('test123@test.com'))

    def test_get_token_by_email_not_found(self):
        """Ensures that the repository returns None if no SubscriptionRequest contains
        the provided email address.
        """
        self.assertEqual(None, repo.get_token_by_email('test123@test.com'))


class SubscriptionAPITestCase(TestCase):
    def setUp(self):
        # create requests
        SubscriptionRequest.objects.create(email='one@test.com')

    def test_subscription_request_api_new_request(self):
        c = Client()
        response = c.post('/api/requests/',
            json.dumps({"email":"newrequest@test.com"}), 
            content_type="application/json")
        self.assertEqual(True, response.json()['data'])

    def test_subscription_request_api_existing_request(self):
        c = Client()
        response = c.post('/api/requests/',
            json.dumps({"email":"one@test.com"}), 
            content_type="application/json")
        self.assertEqual(False, response.json()['data'])

class SubscribersConfigTestCase(TestCase):
    def test_apps(self):
        self.assertEqual(SubscribersConfig.name, 'subscribers')
        self.assertEqual(apps.get_app_config('subscribers').name, 'subscribers')