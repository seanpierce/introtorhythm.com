from django.core.exceptions import ObjectDoesNotExist

from episodes.models import Episode
from .query_helpers import QueryHelpers as Query

class EpisodesRepository:
    """
    Data access layer for episodes
    """

    @staticmethod
    def get_episodes():
        """
        Returns all active episodes as a list id dict objects.
        """

        sql = """
            select e.*, strftime(e.created_at) as created_at
            from episodes_episode e
            where active = 1
            order by e.number desc
        """
        return Query.all(sql)