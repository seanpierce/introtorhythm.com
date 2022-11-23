from django.contrib import admin
from .models import Show, LiveRecording, LiveRecordingAdmin, UpcomingShowAdmin


admin.site.register(Show, UpcomingShowAdmin)
admin.site.register(LiveRecording, LiveRecordingAdmin)