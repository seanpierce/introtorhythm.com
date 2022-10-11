import datetime
from schedule.models import Show
from .query_helpers import QueryHelpers as Query

class ScheduleRepository:
    """
    Data access layer for scheduling
    """

    @staticmethod
    def get_current_show():
        """
        Gets the current show as a dict object.
        """

        sql = """
            select s.*, strftime(s.created_at) as created_at, strftime(s.date) as date
            from schedule_show s
            where date = %s
            and start_time = %s
            and active = 1
        """

        date = datetime.date.today()
        hour = datetime.datetime.now().hour

        return Query.single(sql , [date, hour])

    @staticmethod
    def get_shows(startDate, endDate):
        """
        Returns all active shows that have been scheduled between a provided date range.
        """

        sql = """
            select s.*, strftime(s.created_at) as created_at, strftime(s.date) as date
            from schedule_show s
            where active = 1
            and date >= %s
            and date <= %s
            order by date, start_time
        """

        return Query.many(sql, [startDate, endDate])