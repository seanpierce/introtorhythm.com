from django.test import TestCase

from .models import Subscriber, SubscriptionRequest
from .repository import SubscriberRepository as repo

class SubscriberTestCase(TestCase):
    def setUp(self):
        SubscriptionRequest.objects.create(email='one@test.com')
        SubscriptionRequest.objects.create(email='two@test.com')
        SubscriptionRequest.objects.create(email='three@test.com')
        SubscriptionRequest.objects.create(email='four@test.com')

    def test_get_request_by_token(self):
        req = SubscriptionRequest.objects.get(email='one@test.com')
        selected_req = repo.get_request_by_token(req.token)
        self.assertEqual(req.token, selected_req['token'])
