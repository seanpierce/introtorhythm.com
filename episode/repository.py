from django.db import connection

from .models import Episode

class EpisodeRepository(object):
    
    """Collects a list of number-title combos"""
    def getEpisodeList():
        return Episode.objects.values('number', 'title')