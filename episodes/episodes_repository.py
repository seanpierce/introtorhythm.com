from helpers.query_helper import QueryHelper as Query

class EpisodesRepository:
    """
    Data access layer for episodes
    """

    @staticmethod
    def get_episodes():
        """
        Returns all active episodes as a list id dict objects.
        """

        sql = """
            select 
                e.title,
                e.number,
                e.content,
                e.image,
                e.audio,
                e.tags,
                strftime(e.created_at) as created_at
            from episodes_episode e
            where active = 1
            order by e.number desc
        """

        return Query.many(sql)


    @staticmethod
    def get_episode(number):
        """
        Returns an episode from the database when provided an episode number.
        """

        sql = """
            select e.*, strftime(e.created_at) as created_at
            from episodes_episode e
            where active = 1
            and number = %s
        """

        params = [number]

        return Query.single(sql, params)

    
    @staticmethod
    def get_max_episode_number():
        """
        Returns the largest episode number from the episodes table.
        """

        sql = """
            select max(number) as number from episodes_episode
        """

        return Query.single(sql)
