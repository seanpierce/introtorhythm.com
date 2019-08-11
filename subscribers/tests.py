from django.test import TestCase

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
        req = SubscriptionRequest.objects.get(email='one@test.com')
        selected_req = repo.get_request_by_token(req.token)
        self.assertEqual(req.token, selected_req['token'])

    def test_create_subscriber(self):
        repo.create_subscriber('six@test.com')
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 3)

    def test_remove_subscription_request(self):
        req = SubscriptionRequest.objects.get(email='one@test.com')
        repo.remove_subscription_request(req.token)
        count = SubscriptionRequest.objects.all().count()
        self.assertEqual(count, 2)
