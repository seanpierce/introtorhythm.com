import datetime
from django.contrib import admin
from episodes.models import Episode
from django.utils.html import format_html
from schedule.models import LiveRecording
from schedule.schedule_service import ScheduleService
from episodes.episodes_repository import EpisodesRepository


class LiveRecordingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'info']
    list_display = ['title', 'start_date_time', 'image_tag']
    actions = ['publish_episode']
    exclude = ['image_tag']


    def image_tag(self, obj):
        img_html = """
            <img src="{}" 
                onclick="window.open('{}', '_blank')"
                style="cursor:pointer;max-height:150px;max-width:150px;" />
        """
        try:
            if obj is not None and obj.show_image:
                return format_html(img_html.format(obj.show_image.url, obj.show_image.url))
            else:
                return 'No image available'
        except:
            return 'No image available'

    image_tag.short_description = 'Image'


    def publish_episode(self, request, queryset):
        max_number = int(EpisodesRepository.get_max_episode_number()['number'])
        exp_date = datetime.datetime.now() + datetime.timedelta(30)
        for obj in queryset:
            max_number = max_number + 1
            try:
                live_recording = LiveRecording.objects.get(pk=obj.pk)

                episode = Episode()
                episode.title = live_recording.title
                episode.number = f"{max_number:03}"
                episode.content = ScheduleService.get_episode_content(live_recording)
                episode.image = live_recording.show_image if live_recording.show_image is not None else None
                episode.audio = live_recording.show_recording
                episode.expiration_date = exp_date
                episode.save()

                ScheduleService.process_live_recording(live_recording)
            except:
                max_number = max_number - 1
                continue