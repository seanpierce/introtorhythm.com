import json
from django.http import HttpResponse
from django.views.generic import View
from schedule.repository import ScheduleRepository as repo


class GetShow(View):
    """
    Returns the currently scheduled show.
    """

    def get(self, request):
        """
        GET method for the GetShow api.
        """
        return HttpResponse(json.dumps(repo.get_scheduled_show()), content_type="application/json")


class GetSchedule(View):
    """
    Returns the weekly schedule.
    """

    def get(self, request):
        """
        GET method for the GetSchedule api.
        """
        return HttpResponse(json.dumps(repo.get_schedule()), content_type="application/json")
