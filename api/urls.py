from django.urls import path

from .episodes_api import Recent, All, Search

urlpatterns = [
    path('episodes/recent', Recent.as_view()),
    path('episodes/search', Search.as_view()),
    path('episodes', All.as_view()),
]