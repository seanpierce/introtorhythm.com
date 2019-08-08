from django.db import connection

from .models import Episode

class EpisodeRepository(object):
    """Access layer for episode data."""

    def get_episode_list():
        """Collects a list of number-title combos."""

        return list(Episode.objects
            .filter(active=True)
            .order_by('-number')[:10]
            .values('number', 'title'))


    def get_episode_list_by_number(number):
        most_recent_ten = list(Episode.objects
            .filter(active=True)
            .order_by('-number')[:10]
            .values_list('number', flat=True))
        
        if number in most_recent_ten:
            in_most_recent_ten = True
        else:
            in_most_recent_ten = False

        if not in_most_recent_ten:
            ep = Episode.objects.filter(active=True, number=number).first()

            if ep is None:
                return None

            offest = Episode.objects.filter(pk__lte=ep.pk).count() - 1

            return list(Episode.objects
                .filter(active=True)
                .order_by('-number')[offest:10 + offest]
                .values('number', 'title'))
        else:
            return list(Episode.objects
                .filter(active=True)
                .order_by('-number')[:10]
                .values('number', 'title'))


    def get_current_episode(number=None):
        """Collects all data for the currently selected episode."""

        if number is not None:
            episode = Episode.objects.filter(active=True, number=number).first()

            if episode is None:
                return None
        else:
            episode = Episode.objects.filter(active=True).order_by('-number').first()

        return {
            'id': episode.pk,
            'number': episode.number,
            'title': episode.title,
            'image': str(episode.image),
            'audio': str(episode.audio),
            'content': episode.content
        }
