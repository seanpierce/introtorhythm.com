import datetime
import json
from content.repository import ContentRepository
from django.http import HttpResponse
from django.views.generic import View
from repositories.schedule import ScheduleRepository


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


class RefreshContent(View):
    """
    Polls for updated live content for display in the UI.
    """

    def get(self, request, *args, **kwargs):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        hour = datetime.datetime.now().hour

        response = {
            'bg_image': ContentRepository.get_background_image(),
            'live_callout': ContentRepository.get_live_callout(),
            'now_playing': ScheduleRepository.get_current_show(),
            'schedule_today': [show for show in ScheduleRepository.get_shows(today, today) if show['start_time'] > hour],
            'schedule_tomorrow': ScheduleRepository.get_shows(tomorrow, tomorrow)
        }

        return HttpResponse(json.dumps(response), content_type='application/json')