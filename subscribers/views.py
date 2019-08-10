import json

from django.http import HttpResponse
from django.shortcuts import redirect

from .repository import SubscriberRepository as repo

def confirm(request, token):
    subscription_request = repo.get_request_by_token(token)

    if subscription_request is None:
        return redirect('/?success=false')

    if repo.create_subscriber(subscription_request['email']):
        repo.remove_subscription_request(subscription_request['token'])
        return redirect('/?success=true')
    else:
        return redirect('/?success=false')

