import json

from django.http import HttpResponse
from django.shortcuts import redirect

from .repository import SubscriberRepository as repo

def confirm(request, token):
    """The confirm method is a view that operates as a simple GET api method.
    
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
    subscription_request = repo.get_request_by_token(token)

    if subscription_request is None:
        return redirect('/?success=false')

    if repo.create_subscriber(subscription_request['email']):
        repo.remove_subscription_request(subscription_request['token'])
        return redirect('/?success=true')
    else:
        return redirect('/?success=false')

