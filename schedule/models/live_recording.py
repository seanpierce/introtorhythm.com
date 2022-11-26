from django.db import models
from django.dispatch import receiver


class LiveRecording(models.Model):
    """
    Django model for the schedule.LiveRecording ORM/ data table.
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    info = models.TextField(default=None, blank=True, null=True)
    start_date_time = models.DateTimeField(null=True)
    show_image = models.ImageField(upload_to='live-recordins/images/', max_length=500, blank=True)
    show_recording = models.FileField(upload_to="live-recordings/audio", max_length=500, blank=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['start_date_time']

    def __str__(self):
        return self.title

    def complete(self):
        if (
            self.title is not None and 
            self.info is not None and
            self.start_date_time is not None and
            self.show_image is not None and
            self.show_recording is not None
        ):
            return True
        else:
            return False



@receiver(models.signals.pre_save, sender=LiveRecording)
def pre_save(sender, instance, **kwargs):
    """
    Method that is executed before the instance is saved to the database.
    """
    auto_delete_files_on_change(instance)


@receiver(models.signals.post_delete, sender=LiveRecording)
def post_delete(sender, instance, using, **kwargs):
    """
    Method that is executed after the instance is deleted from the database.
    """
    delete_files_when_instance_is_deleted(instance)


def auto_delete_files_on_change(instance):
    """
    Deletes old image and audio files from filesystem (AWS S3)
    when corresponding `Image`, or `File` object is updated
    with new file.
    """
    if not instance.pk:
        return None

    live_recording = LiveRecording.objects.get(pk=instance.pk)

    try:
        old_image_file = live_recording.show_image
        old_audio_file = live_recording.show_recording
    except:
        return None

    new_image_file = instance.show_image
    new_audio_file = instance.show_recording

    if not old_image_file == new_image_file:
        old_image_file.delete(save=False)

    if not old_audio_file == new_audio_file:
        old_audio_file.delete(save=False)


def delete_files_when_instance_is_deleted(instance):
    """
    Deletes image and audio files from filesystem (AWS S3)
    when corresponding record is deleted.
    """
    # if the instance is not processed, then delete the media assets
    if not instance.processed:
        instance.show_image.delete(save=False)
        instance.show_recording.delete(save=False)