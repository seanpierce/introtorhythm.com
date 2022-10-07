import json
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from subscribers.repository import SubscriberRepository as repo
from subscribers.emails import SubscriberEmails as email


class ConfirmSubscription(View):
    def get(self, request, *args, **kwargs):
        """Creates a Subscriber record when provided a SubscriptionRequest token.

        Process:
            * find a subscription request which matches the token provided
            * create a subscriber based on the data collected in the the
                subscription request
            * delete the original subscription request
            * redirect the user to the main page, with a query string indicating
                success or failure

        Path:
            /api/requests/confirm/[token]

        Args:
            token: a string value representing a token found in a subscription request record.

        Returns:
            Returns a redirect response which includes a url parameter indicating
            success or failure of the process.
        """
        token = self.kwargs['token']
        subscription_request = repo.get_request_by_token(token)

        if subscription_request is None:
            return redirect('%s/?success=false' %(settings.HOST_URL))

        if repo.create_subscriber(subscription_request['email']):
            repo.remove_subscription_request(subscription_request['token'])
            return redirect('%s/?success=true' %(settings.HOST_URL))
        else:
            return redirect('%s/?success=false' %(settings.HOST_URL))


@method_decorator(csrf_exempt, name='dispatch')
class RequestSubscription(View):
    def post(self, request, *args, **kwargs):
        """Creates a SubscriptionRequest record in the database,
        then sends a confirmation email to the email address provided in the request.

        Args:
            email: string representing the email address for the subscription request.

        Returns:
            A boolean value indicating the success or failure of the process.
        """

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[-1].strip()
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        body = json.loads(request.body.decode('utf-8'))

        if repo.create_subscription_request(body['email'], ip_address):
            token = repo.get_token_by_email(body['email'])
            email.send_request_confirmation_email(body['email'], token)
            return HttpResponse(json.dumps({'data': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'data': False}), content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class Unsubscribe(View):
    def post(self, request, *args, **kwargs):
        """Removes a subscriber from the database when provided an email address.

        Args:
            email: string representing the email address for the subscription request.

        Returns:
            A boolean value indicating the success or failure of the process.
        """
        body = json.loads(request.body.decode('utf-8'))

        if repo.unsubscribe(body['email']):
            return HttpResponse(json.dumps(True), content_type="application/json")
        else:
            return HttpResponse(json.dumps(False), content_type="application/json")