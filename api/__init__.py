import configparser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class APIView(View):
    """
    Base class for custom API view.
    """
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(APIView, self).dispatch(*args, **kwargs)

    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('./env.ini')
        self.SCHEDULE_AUTH_SECRET = config.get('Secrets', 'SCHEDULE_AUTH')

    
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
        configured_secret = getattr(self, configured_key, None)
        if configured_secret is None:
            return False

        try:
            # example X-SCHEDULE-AUTH-SECRET
            secret = request.headers['X-%s-SECRET' %(key)]
            valid = secret == configured_secret
            return valid
        except Exception as ex:
            return False