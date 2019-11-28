from django.db.models import Q

from .models import Episode

class EpisodeRepository:
    """
    Access layer for accessing episode data.
    """

    @staticmethod
    def get_episodes(take=None):
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
        return list(Episode.objects.filter(
                Q(number__contains=search_text) |
                Q(title__contains=search_text)  |
                Q(content__contains=search_text)
            ).order_by('-number')
            .values('number', 'title', 'content', 'image', 'audio'))

    @staticmethod
    def get_episode_by_number(number):
        episode = Episode.objects.filter(active=True).order_by('-number').first()
        return {
            'number': episode.number,
            'title': episode.title,
            'content': episode.content,
            'image': episode.image.url,
            'audio': episode.audio.url
        }