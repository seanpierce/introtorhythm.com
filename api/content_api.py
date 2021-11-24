import json
from . import APIView
from content.repository import ContentRepository as repo


class Info(APIView):
    """
    Returns 'Info' content.
    """
    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        data = repo.get_content_by_name(name)
        return self.Response(data)


class BackgroundImage(APIView):
    """
    Returns the background image url for the configured background image.
    """
    def get(self, request, *args, **kwargs):
        data = repo.get_background_image()
        return self.Response(data)