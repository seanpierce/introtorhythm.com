from django.urls import path
from .views.content import get_content
from .views.schedule import initiate_show

urlpatterns = [
    path('content/', get_content, name="get_content"),
    path('schedule/initiate-show/', initiate_show, name='initiate_show')
]