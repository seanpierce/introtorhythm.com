from . import APIView
from repositories.episodes import EpisodesRepository as repo


class All(APIView):
    """
    Returns all episode data.
    """

    def get(self, request, *args, **kwargs):
        data = repo.get_episodes()
        return self.Response(data)


class Single(APIView):
    """
    Returns a single episode from the database when provided an episode number.
    """

    def post(self, request, *args, **kwargs):
        payload = self.GetPayload(request, ['number'])
        data = repo.get_episode(payload.number)
        return self.Response(data)
