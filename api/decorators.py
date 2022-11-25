from django.http import HttpResponseBadRequest
from .api_helper import ApiHelper

def header_auth(secret:str, header:str):
    """
    Class-based API view method decorator used to validate secrets
    passed in through the request headers.
    """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if not ApiHelper.verify_header_secret(secret, header, request):
                return HttpResponseBadRequest()
            else:
                return func(request, *args, **kwargs)
                
        return wrapper

    return decorator