import json

from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from content.repository import ContentRepository as repo

class Info(View):
    """
    Returns 'Info' content.
    """
    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        return HttpResponse(json.dumps(repo.get_content_by_name(name)), content_type="application/json")


class BackgroundImage(View):
    """
    Returns the background image url for the configured background image.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_background_image()), content_type="application/json")