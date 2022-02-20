import json
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View


class APIView(View):
    """
    Base class for custom API view.
    """
    
    def Response(self, data, status=200):
        try:
            return HttpResponse(json.dumps(data), status=status, content_type='application/json')
        except Exception as e:
            return HttpResponse('Unable to create API response', status=500, content_type='application/json')


    def GetPayload(self, request, params):
        payload = {}
        body = json.loads(request.body.decode('utf-8'))
        
        for param in params:
            payload[param] = body[param]

        return payload

    
    def secret_is_valid(self, key, request):
        """
        Looks for a header secret matching the name of a supplied key.
        If found, validates that the value of the header matches what is in the 
        application's configuration.
        """

        if key is None:
            return False

        # example SCHEDULE_AUTH_SECRET
        configured_key = '%s_SECRET' %(key.replace('-', '_'))
        configured_secret = getattr(settings, configured_key, None)
        if configured_secret is None:
            return False

        try:
            # example X-SCHEDULE-AUTH-SECRET
            secret = request.headers['X-%s-SECRET' %(key)]
            valid = secret == configured_secret
            return valid
        except Exception as ex:
            return False