from .episodes_repository import EpisodesRepository


class EpisodesService:

    @staticmethod
    def get_max_episode_number() -> str:
        """
        Gets the max episode number from the database. 
        Returns the value as a string padded with leading zeros.
        """
        max_number = int(EpisodesRepository.get_max_episode_number()['number'])
        return f"{max_number:03}"