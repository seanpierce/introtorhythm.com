from django.db import connection

from .models import Episode

class EpisodeRepository(object):
    """Access layer for episode data."""

    def get_episode_list():
        """Collects a list of number-title combos.
        
        Returns:
            A list of the ten most recent number-title combos.
            Example [{'number': '001', 'title': 'First Episode'}, ...]
        """

        return list(Episode.objects
            .filter(active=True)
            .order_by('-number')[:10]
            .values('number', 'title'))


    def get_episode_list_by_number(number):
        """Collects a liist of number-title combos, offset by a specified episode.
        
        Args:
            number: a value representing an episode number, supplied by the url in the request.

        Returns:
            A list of ten number-title combos.
            Example: [{'number': '001', 'title': 'First Episode'}, ...]
        """
        most_recent_ten = list(Episode.objects
            .filter(active=True)
            .order_by('-number')[:10]
            .values_list('number', flat=True))
        
        if number in most_recent_ten:
            in_most_recent_ten = True
        else:
            in_most_recent_ten = False

        if not in_most_recent_ten:
            return list(Episode.objects
                .filter(active=True, number__gte=number)
                .order_by('number')[:10]
                .values('number', 'title'))[::-1]
        else:
            return list(Episode.objects
                .filter(active=True)
                .order_by('-number')[:10]
                .values('number', 'title'))


    def get_current_episode(number=None):
        """Collects all data for the currently selected episode.
        
        Args:
            number: an optional argument passed in through the url in the request
            which should correspond with an episode's number in the database.

        Returns:
            A dict containing key-value pairs corresponding to the selected episode's data.
            Example: {
                'id': 1,
                'number': '001',
                'title': 'First Episode',
                ...
            }
        """

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
