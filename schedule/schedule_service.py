import datetime

from .models.live_recording import LiveRecording


class ScheduleService:

    @staticmethod
    def get_date_string_from_filename(filename:str) -> str:
        """
        When supplied a filename, returns a string 
        representing the date a scheduled show took place.
        example input: ITR_rec_20221123-170448.mp3
        example output: 2022-11-23
        """

        output = filename.replace('ITR_rec_', '')
        output = output.split('-')[0]
        output = f"{output[:4]}-{output[4:6]}-{output[6:]}"
        return output


    @staticmethod
    def get_hour_from_filename(filename:str) -> int:
        """
        When supplied a filename, returns an int 
        representing the start hour of a scheduled show.
        example input: ITR_rec_20221123-170448.mp3
        example output: 17
        """

        output = filename.replace('ITR_rec_', '')
        output = output.split('-')

        hour = int(output[1][:2])
        minutes = int(output[1][2:4])

        # set threshold for rounding up if
        # the recording started slightly before the hour
        if minutes > 50:
            hour = hour + 1

        return hour


    @staticmethod
    def save_live_recording(show:dict, file):
        """
        Persists a LiveRecording to the database.
        """

        live_recording = LiveRecording()
        live_recording.title = show['title']
        live_recording.start_date_time = datetime.datetime.strptime(show['start_date_time'], '%Y-%m-%d %X')
        live_recording.info = ScheduleService.get_episode_content(live_recording)

        if show['show_image'] is not None:
            live_recording.show_image = show['show_image']

        if file is not None:
            live_recording.show_recording.save(file.name, file)

        live_recording.save()


    @staticmethod
    def save_live_recording_without_show(file):
        """
        If a show is not found based on the file's name,
        create a LiveRecording with blank details.
        """

        live_recording = LiveRecording()
        live_recording.title = None
        live_recording.start_date_time = None
        live_recording.info = None
        live_recording.show_image = None
        live_recording.show_recording.save(file.name, file)
        live_recording.save()

    
    @staticmethod
    def get_episode_content(live_recording:LiveRecording) -> str:
        """
        Concatenates basic placeholder content for a live recording turnde episode.
        """
        air_date = live_recording.start_date_time.strftime("%m/%d/%Y")
        return f'"{live_recording.title}" streamed live from Musique Plastique on {air_date}.'


    @staticmethod
    def process_live_recording(live_recording:LiveRecording):
        """
        Flags the record as 'proccessed' in the database before deleting.
        This happens to prevent the image and audio assets from being 'cleaned-up'
        when the instance is deleted.
        """
        live_recording.processed = True
        live_recording.save()
        live_recording.delete()