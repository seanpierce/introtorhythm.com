import json

from django.http import HttpResponse
from django.views.generic import View

from .repository import EpisodeRepository as repo

class EpisodesAPI(View):
    """API controller for handling episode data.
    """

    def get(self, request, *args, **kwargs):
        """Get method for handling episode data.

        Returns: a JSON array of episode numbers and titles in descending order.
        """

        data = {
            'episodes': repo.get_all_episode_list()
        }
        return HttpResponse(json.dumps({'data': data}), content_type="application/json")