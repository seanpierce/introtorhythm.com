from django.db import connection


class QueryHelper:
    """
    Helper class for serializing django query sets.
    """

    @staticmethod
    def many(sql, params=None):
        """
        Returns all rows from a cursor as a dict.
        Args: 
            sql (string): A string that represents a sql query.
            params (list): A list of parameters to serialize into the query.
        Returns:
            result (list): A list of dict objects that represent each row returned by the database query.
        """

        with connection.cursor() as cursor:

            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            records = cursor.fetchall()

            if not records:
                return []

            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in records
            ]


    @staticmethod
    def single(sql, params=None):
        """
        Returns one row from a cursor as a dict.
        Args: 
            sql (string): A string that represents a sql query.
            params (list): A list of parameters to serialize into the query.
        Returns:
            result (dict): A dict object that represents a row returned by the database query.
        """

        with connection.cursor() as cursor:

            if params is not None:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            record = cursor.fetchone()

            if record is None:
                return None

            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, record))


    @staticmethod
    def insert(sql, params):
        """
        Inserts data into the database.
        Args: 
            sql (string): A string that represents a sql query.
            params (list): A list of parameters to serialize into the query.
        Returns:
            id (int): last row id of the insert statement.
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, params)         
            return cursor.fetchone()[0]