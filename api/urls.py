from django.urls import path

from .episodes_api import Recent, All, Search, Episode, Featured, SearchTags
from .content_api import Info
from .subscribers_api import ConfirmSubscription, RequestSubscription, Unsubscribe

urlpatterns = [
    path('episodes/recent', Recent.as_view()),
    path('episodes/featured', Featured.as_view()),
    path('episodes/search', Search.as_view()),
    path('episodes/search/tag', SearchTags.as_view()),
    path('episodes/<number>', Episode.as_view()),
    path('episodes', All.as_view()),
    path('content/<name>', Info.as_view()),
    path('subscribers/request', RequestSubscription.as_view()),
    path('subscribers/confirm/<token>', ConfirmSubscription.as_view()),
    path('subscribers/unsubscribe', Unsubscribe.as_view()),
]