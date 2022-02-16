import json
from django.http import HttpResponse
from django.views.generic import View
from repositories.schedule import ScheduleRepository as repo


class GetShow(View):
    """
    Returns the currently scheduled show.
    """

    def get(self, request):
        """
        GET method for the GetShow api.
        """
        return HttpResponse(json.dumps(repo.get_current_show()), content_type="application/json")


class GetSchedule(View):
    """
    Returns the weekly schedule.
    """

    def get(self, request):
        """
        GET method for the GetSchedule api.
        """
        return HttpResponse(json.dumps(repo.get_shows()), content_type="application/json")
