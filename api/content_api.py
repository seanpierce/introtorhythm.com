import json
from content.repository import ContentRepository as repo
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class Info(View):
    """
    Returns 'Info' content.
    """
    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        data = repo.get_content_by_name(name)
        return HttpResponse(json.dumps(data), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class BackgroundImage(View):
    """
    Returns the background image url for the configured background image.
    """
		
    def get(self, request, *args, **kwargs):
        data = repo.get_background_image()
        return HttpResponse(json.dumps(data), content_type='application/json')