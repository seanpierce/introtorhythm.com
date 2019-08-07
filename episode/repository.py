from django.db import connection

from .models import Episode

class EpisodeRepository(object):
    """Access layer for episode data."""

    def get_episode_list():
        """Collects a list of number-title combos."""
        return list(Episode.objects.values('number', 'title'))

    def get_current_episode(number=None):
        """Collects all data for the currently selected episode."""

        if number is not None:
            episode = Episode.objects.filter(number=number).first()
            if episode is None:
                return None
        else:
            episode = Episode.objects.order_by('-number').first()

        return {
            'id': episode.pk,
            'number': episode.number,
            'title': episode.title,
            'image': str(episode.image),
            'audio': str(episode.audio),
            'content': episode.content
        }
