"""
Routes for the subscriber API. 
"""
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .repository import SubscriberRepository as repo
from .emails import SubscriberEmails as email

class SubscrptionConfirmationAPI(View):
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
            return redirect('/?success=false')

        if repo.create_subscriber(subscription_request['email']):
            repo.remove_subscription_request(subscription_request['token'])
            return redirect('/?success=true')
        else:
            return redirect('/?success=false')


class SubscriptionRequestAPI(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Add decorator to internal class method to
        ignore the pressence of a csrf token/ cookie in the requrest.
        """
        return super(SubscriptionRequestAPI, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a SubscriptionRequest record in the database,
        then sends a confirmation email to the email address provided in the request.

        Args:
            email: string representing the email address for the subscription request.

        Returns:
            A boolean value indicating the success or failure of the process.
        """
        body = json.loads(request.body.decode('utf-8'))

        if repo.create_subscription_request(body['email']):
            token = repo.get_token_by_email(body['email'])
            email.send_request_confirmation_email(body['email'], token)
            return HttpResponse(json.dumps({'data': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'data': False}), content_type="application/json")


class UnsubscribeAPI(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Add decorator to internal class method to
        ignore the pressence of a csrf token/ cookie in the requrest.
        """
        return super(UnsubscribeAPI, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Removes a subscriber from the database when provided an email address.

        Args:
            email: string representing the email address for the subscription request.

        Returns:
            A boolean value indicating the success or failure of the process.
        """
        body = json.loads(request.body.decode('utf-8'))

        if repo.unsubscribe(body['email']):
            return HttpResponse(json.dumps({'data': True}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'data': False}), content_type="application/json")


def unsubscribe(request):
    """
    """

    data = {
    }

    return render(request, 'app.html', {
        'data': data,
        'title': 'Unsubscribe :('
    })