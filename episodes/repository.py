from django.db.models import Q

from .models import Episode

class EpisodeRepository:
    """
    Access layer for writing and reading episode data.
    """

    @staticmethod
    def get_episodes(take=None):
        """
        Returns a list of episode data.
        """

        if take is None:
            return list(Episode.objects
                .filter(active=True)
                .order_by('-number')
                .values('number', 'title', 'content', 'image', 'audio'))
        else:
            return list(Episode.objects
                .filter(active=True)
                .order_by('-number')[:take]
                .values('number', 'title', 'content', 'image', 'audio'))

    @staticmethod
    def search(search_text):
        """
        Returns a list of Active episode data if
         an episode's number, title, or content contains a user-inputted search term.
        """

        return list(Episode.objects.filter(
                Q(number__contains=search_text) |
                Q(title__contains=search_text)  |
                Q(content__contains=search_text)
            ).filter(active=True)
            .order_by('-number')
            .values('number', 'title', 'content', 'image', 'audio'))

    @staticmethod
    def get_episode_by_number(number):
        """
        Returns data for a single episode matching
         the number value pulled from the url.
        """

        return Episode.objects.filter(active=True, number=number).order_by('-number').values('number', 'title', 'content', 'image', 'audio').first()