import json
from django.http import HttpResponse
from django.views.generic import View
from .api_helper import ApiHelper
from .decorators import header_auth
from repositories.schedule import ScheduleRepository


class ProcessLiveRecording(View):
    """
    Based on a posted file's filename, collects data from the scheduled shows tables 
    to create and save a new instance of a LiveRecording.
    """

    @header_auth('PROCESS_LIVE_RECORDING_AUTH', 'X-PROCESS-LIVE-RECORDING-AUTH-SECRET')
    def post(self, request):

        file = request.FILES['recording']
        
        # get date and hour of show
        date_string = ApiHelper.get_date_string_from_filename(file.name)
        hour = ApiHelper.get_hour_from_filename(file.name)
        
        # reference shows table to get content
        show = ScheduleRepository.get_show_by_date_and_hour(date_string, hour)

        # save live recording to db
        if show is not None:
            ApiHelper.save_live_recording(show, file)

        return HttpResponse(json.dumps(True), content_type='application/json')