from django.db import connection

class QueryHelpers:
    """
    Helper class for serializing query sets after collection from the database.
    """

    @staticmethod
    def many(sql, params=None):
        """
        Return all rows from a cursor as a dict.

        Args: 
            sql (string): A string that represents a sql query.
            params (list): A list of parameters to serialize into the query.

        Returns:
            list: A list of dictionaries that represent each row returned from the database.
        """
        with connection.cursor() as cursor:

            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]


    @staticmethod
    def single(sql, params=None):
        """
        Return one from a cursor as a dict.

       Args: 
            sql (string): A string that represents a sql query.
            params (list): A list of parameters to serialize into the query.

        Returns:
            dict: a Dictionary that represent the row returned from the database.
        """
        with connection.cursor() as cursor:

            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, cursor.fetchone()))