import datetime
import json
from dateutil import parser
from django.http import HttpResponse
from django.views.generic import View
from content.content_repository import ContentRepository
from schedule.schedule_repository import ScheduleRepository


class Info(View):
    """
    Returns 'Info' content.
    """
    def get(self, request, *args, **kwargs):
        data = ContentRepository.get_site_info()
        return HttpResponse(json.dumps(data), content_type='application/json')


class BackgroundImage(View):
    """
    Returns the background image url for the configured background image.
    """
		
    def get(self, request, *args, **kwargs):
        data = ContentRepository.get_background_image()
        return HttpResponse(json.dumps(data), content_type='application/json')


class CallInNumber(View):
    """
    API endpoint used to fetch the current call-in number that is set in the admin portal.
    """

    def get(self, request, *args, **kwargs):
        data = ContentRepository.get_call_in_number()
        return HttpResponse(json.dumps(data), content_type='application/json')        


class RefreshContent(View):
    """
    Polls for updated live content for display in the UI.
    """

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        one_month_from_now = tomorrow + datetime.timedelta(days=30)

        response = {
            'bg_image': ContentRepository.get_background_image(),
            'live_callout': ContentRepository.get_live_callout(),
            'now_playing': ScheduleRepository.get_current_show(),
            'schedule_today': [show for show in ScheduleRepository.get_shows(today, today) if parser.parse(show['start_date_time']) > datetime.datetime.now()],
            'schedule_upcoming': ScheduleRepository.get_shows(tomorrow, one_month_from_now)
        }

        return HttpResponse(json.dumps(response), content_type='application/json')