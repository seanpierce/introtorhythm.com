from django.contrib import admin
from .models import Show, LiveRecording, LiveRecordingAdmin, UpcomingShowAdmin


admin.site.register(Show, UpcomingShowAdmin)
# commenting this out to avoid confusion because its not being used
# sean pierce 01-20-2023
# admin.site.register(LiveRecording, LiveRecordingAdmin)