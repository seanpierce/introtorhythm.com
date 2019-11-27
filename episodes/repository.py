from .models import Episode

class EpisodeRepository:
    """
    Access layer for accessing episode data.
    """

    @staticmethod
    def get_episodes(take):
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