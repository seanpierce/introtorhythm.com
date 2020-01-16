import datetime

from .models import Show

class ScheduleRepository:
    """
    Access layer for scheduled show data.
    """

    @staticmethod
    def get_scheduled_show():
        """
        Returns a show that is scheduled to start on the current day and hour.
        """
        current_day = datetime.datetime.now().weekday()
        current_hour = datetime.datetime.now().hour

        return Show.objects.filter(
            active=True,
            pre_record=True,
            day=current_day,
            start_time=current_hour
        ).values('title', 'audio').first()

    @staticmethod
    def get_schedule():
        """
        Returns the weekly schedule of shows
        """

        return list(
            Show.objects.filter(active=True).order_by(
                'day', 'start_time'
            ).values(
                'day', 'start_time', 'title'))
