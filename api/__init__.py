import json
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class APIView(View):
    
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