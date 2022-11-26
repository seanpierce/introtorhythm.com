import configparser
import datetime

from schedule.models.live_recording import LiveRecording
from schedule.models.live_recording_admin import get_episode_content


class ApiHelper:
    """
    Helper class for API processes.
    """

    @staticmethod
    def verify_header_secret(secret:str, header:str, request) -> bool:
        """
        Method used to verify supplied header secrets against configured variables.
        """
        config = configparser.RawConfigParser()
        config.read('./env.ini')
        config_secret = config.get('Secrets', secret)
        header_secret = request.request.headers[header]
        return config_secret == header_secret


    @staticmethod
    def get_date_string_from_filename(filename:str) -> str:
        """
        When supplied a filename, returns a string 
        representing the date a scheduled show took place.
        ex: ITR_rec_20221123-090448.mp3
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
        ex: ITR_rec_20221123-090448.mp3
        """

        output = filename.replace('ITR_rec_', '')
        output = output.split('-')

        hour = int(output[1][:2])
        minutes = int(output[1][2:4])

        # set threshold for rounding up if
        # the stream started slightly before the hour
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
        live_recording.show_image = show['show_image'] if show['show_image'] is not None else None
        live_recording.show_recording.save(file.name, file)
        live_recording.start_date_time = datetime.datetime.strptime(show['start_date_time'], '%Y-%m-%d %X')
        live_recording.info = get_episode_content(live_recording)
        live_recording.save()