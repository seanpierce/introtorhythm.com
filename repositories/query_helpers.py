from django.db import connection

class QueryHelpers:
    """
    Helper class for serializing query sets after collection from the database.
    """

    @staticmethod
    def all(sql):
        """
        Return all rows from a cursor as a dict.

        Args: 
            sql - A string that represents a sql query
        """
        with connection.cursor() as cursor:
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

    @staticmethod
    def single(sql):
        """
        Return one from a cursor as a dict.

        Args: 
            sql - A string that represents a sql query
        """
        with connection.cursor() as cursor:
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, cursor.fetchone()))