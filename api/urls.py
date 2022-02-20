from django.urls import path
from .episodes_api import All, Single
from .content_api import Info, BackgroundImage
from .subscribers_api import ConfirmSubscription, RequestSubscription, Unsubscribe
from .schedule_api import GetShow, GetSchedule, Initiate

urlpatterns = [
    path('episodes', All.as_view()),
    path('episode', Single.as_view()),
    path('content/backgroundimage', BackgroundImage.as_view()),
    path('content/<name>', Info.as_view()),
    path('subscribers/request', RequestSubscription.as_view()),
    path('subscribers/confirm/<token>', ConfirmSubscription.as_view()),
    path('subscribers/unsubscribe', Unsubscribe.as_view()),
    path('schedule', GetSchedule.as_view()),
    path('schedule/show', GetShow.as_view()),
    path('schedule/initiate-scheduler', Initiate.as_view())
]