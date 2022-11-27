import configparser
from django.http import HttpResponseBadRequest

def header_auth(secret:str, header:str):
    """
    Class-based API view method decorator used to validate secrets
    passed in through the request headers.
    """
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            config = configparser.RawConfigParser()
            config.read('./env.ini')
            config_secret = config.get('Secrets', secret)
            header_secret = request.request.headers[header]
            valid = config_secret == header_secret
            if not valid:
                return HttpResponseBadRequest()
            else:
                return func(request, *args, **kwargs)
                
        return wrapper

    return decorator