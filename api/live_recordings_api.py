import json
from django.http import HttpResponse
from django.views.generic import View
from .decorators import header_auth


class ProcessLiveRecording(View):
    """
    Initiates the schedule process which checks for a
    shceudled show in the database. If found, the process
    reconfigures ezstream to run the scheduled show's file.
    """
    
    @header_auth('PROCESS_LIVE_RECORDING_AUTH', 'X-PROCESS-LIVE-RECORDING-AUTH-SECRET')
    def post(self, request):

        payload = json.loads(request.body)
        return HttpResponse(json.dumps(payload), content_type='application/json')