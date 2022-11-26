import datetime
from django.contrib import admin
from episodes.models import Episode
from django.utils.html import format_html
from schedule.models import LiveRecording
from repositories.episodes import EpisodesRepository


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
                episode.content = get_episode_content(episode, live_recording)
                episode.image = live_recording.show_image if live_recording.show_image is not None else None
                episode.audio = live_recording.show_recording
                episode.expiration_date = exp_date
                episode.save()
                process_live_recording(live_recording)
            except:
                max_number = max_number - 1
                continue


def get_episode_content(live_recording:LiveRecording):
    if not live_recording.pk:
        air_date = live_recording.start_date_time.strftime("%m/%d/%Y")
    else:
        air_date = live_recording.start_date_time.strftime("%m/%d/%Y")
        
    return f'"{live_recording.title}" streamed live from Musique Plastique on {air_date}.'


def process_live_recording(live_recording:LiveRecording):
    """
    Flags the record as 'proccessed' in the database before deleting.
    This happens to prevent the image and audio assets from being 'cleaned-up'
    when the instance is deleted.
    """
    live_recording.processed = True
    live_recording.save()
    live_recording.delete()