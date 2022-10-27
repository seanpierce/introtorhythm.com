from django.urls import path
from . import contact_api
from . import content_api
from . import episodes_api
from . import schedule_api
from . import subscribers_api

urlpatterns = [
    path('episodes', episodes_api.All.as_view()),
    path('episode', episodes_api.Single.as_view()),
    path('content/backgroundimage', content_api.BackgroundImage.as_view()),
    path('content/<name>', content_api.Info.as_view()),
    path('subscribers/request', subscribers_api.RequestSubscription.as_view()),
    path('subscribers/confirm/<token>', subscribers_api.ConfirmSubscription.as_view()),
    path('subscribers/unsubscribe', subscribers_api.Unsubscribe.as_view()),
    path('schedule', schedule_api.GetSchedule.as_view()),
    path('schedule/show', schedule_api.GetShow.as_view()),
    path('schedule/initiate-scheduler', schedule_api.Initiate.as_view()),
    path('contact/booking', contact_api.SendBookingRequest.as_view())
]