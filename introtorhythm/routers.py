from rest_framework import routers
from episode.viewsets import EpisodeViewSet

router = routers.DefaultRouter()
router.register(r'episode', EpisodeViewSet)