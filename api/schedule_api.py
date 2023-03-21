import datetime
import json
from django.http import HttpResponse
from django.views.generic import View
from schedule.schedule_repository import ScheduleRepository as repo
from schedule import scheduler


class GetShow(View):
    """
    Returns the currently scheduled show.
    """

    def get(self, request):
        data = repo.get_current_show()
        return HttpResponse(json.dumps(data), content_type='application/json')


class GetSchedule(View):
    """
    Returns the monthly schedule.
    """

    def get(self, request):
        startDate = datetime.date.today()
        endDate = startDate + datetime.timedelta(days=30) 
        data = repo.get_shows(startDate, endDate)

        response = {
            'shows': data,
            'startDate': startDate,
            'endDate': endDate
        }
        return HttpResponse(json.dumps(response, default=str), content_type='application/json')
