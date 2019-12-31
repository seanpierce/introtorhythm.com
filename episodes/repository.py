from django.db.models import Q

from .models import Episode

class EpisodeRepository:
    """
    Access layer for writing and reading episode data.
    """

    @staticmethod
    def get_episodes():
        """
        Returns a list of episode data.
        """
        return list(Episode.objects
            .filter(active=True)
            .order_by('-number')
            .values('number', 'title', 'image', 'tags'))

    @staticmethod
    def search(search_text):
        """
        Returns a list of Active episode data if
         an episode's number, title, or content contains a user-inputted search term.
        """

        return list(Episode.objects.filter(
                Q(number__contains=search_text) |
                Q(title__contains=search_text)  |
                Q(content__contains=search_text)|
                Q(tags__contains=search_text)
            ).filter(active=True)
            .order_by('-number')
            .values('number', 'title', 'image', 'tags'))

    @staticmethod
    def search_by_tag(tag):
        """
        Returns a list of Active episode data if
         an episode contains a provided tag.
        """

        return list(Episode.objects.filter(
                Q(tags__contains=tag)
            ).filter(active=True)
            .order_by('-number')
            .values('number', 'title', 'image', 'tags'))

    @staticmethod
    def get_episode_by_number(number):
        """
        Returns data for a single episode matching
         the number value pulled from the url.
        """

        return Episode.objects.filter(active=True, number=number).order_by('-number').values('number', 'title', 'content', 'tags', 'image', 'audio').first()

    @staticmethod
    def get_featured_episodes():
        """
        Returns a list of data for episodes that are marked as 'featured'.
        """

        return list(Episode.objects
            .filter(active=True, featured=True)
            .values('number', 'title', 'image', 'tags'))

    @staticmethod
    def paginate(offset, take):
        return list(Episode.objects
            .filter(active=True)
            .order_by('-number')[offset:][:take]
            .values('number', 'title', 'image', 'tags'))