import configparser
import json
from django.http import HttpResponse
from django.views.generic import View
from braces.views import CsrfExemptMixin
from repositories.schedule import ScheduleRepository as repo
from schedule import scheduler
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class GetShow(View):
    """
    Returns the currently scheduled show.
    """

    def get(self, request):
        data = repo.get_current_show()
        return HttpResponse(json.dumps(data), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class GetSchedule(View):
    """
    Returns the weekly schedule.
    """

    def get(self, request):        
        data = repo.get_shows()
        return HttpResponse(json.dumps(data), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Initiate(CsrfExemptMixin, View):
    """
    Initiates the schedule process which checks for a
    shceudled show in the database. If found, the process
    reconfigures ezstream to run the scheduled show's file.
    """

    def post(self, request):
        config = configparser.RawConfigParser()
        config.read('./env.ini')
        schedule_auth_secret = config.get('Secrets', 'SCHEDULE_AUTH')
        secret = request.headers['X-SCHEDULE-AUTH-SECRET']
        valid = secret == schedule_auth_secret

        if not valid:
            return self.Response(None, 401)

        outcome = scheduler.run()
        return HttpResponse(json.dumps(outcome), content_type='application/json')
