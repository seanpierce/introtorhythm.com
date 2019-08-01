from rest_framework import viewsets
from .models import Episode
from .serializers import EpisodeSerializer

# A viewset is synonymous to a Controller or Resource

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer