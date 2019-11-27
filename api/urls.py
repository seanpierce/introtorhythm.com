from django.urls import path

from .episodes_api import RecentEpisodes

urlpatterns = [
    path('episodes/recent', RecentEpisodes.as_view()),
]