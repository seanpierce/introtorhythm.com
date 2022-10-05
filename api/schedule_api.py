import json
from django.http import HttpResponse
from braces.views import CsrfExemptMixin
from repositories.schedule import ScheduleRepository as repo
from schedule import scheduler
from . import APIView


class GetShow(APIView):
    """
    Returns the currently scheduled show.
    """

    def get(self, request):
        data = repo.get_current_show()
        return HttpResponse(json.dumps(data), content_type='application/json')


class GetSchedule(APIView):
    """
    Returns the weekly schedule.
    """

    def get(self, request):        
        data = repo.get_shows()
        return HttpResponse(json.dumps(data), content_type='application/json')


class Initiate(CsrfExemptMixin, APIView):
    """
    Initiates the schedule process which checks for a
    shceudled show in the database. If found, the process
    reconfigures ezstream to run the scheduled show's file.
    """

    def post(self, request):
        if not self.secret_is_valid('SCHEDULE-AUTH', request):
            return self.Response(None, 401)

        outcome = scheduler.run()
        return HttpResponse(json.dumps(outcome), content_type='application/json')
