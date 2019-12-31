from django.apps import apps
from django.test import TestCase

from .apps import EpisodesConfig
from .models import Episode
from .repository import EpisodeRepository as repo


class EpisodeTestCase(TestCase):
    def setUp(self):
        """
        Creates test data.
        We can assert that:
            - there are 13 episodes in total.
            - 12 episode are active
            - 'Episode 013' is the most recent
            - 'Episode 001' is the first episode (although not 'Active')
            - 'Episode 002' is the first 'Active' episode
        """

        Episode.objects.create(number='001', title='Episode 1', active=False)
        Episode.objects.create(number='002', title='Episode 2')
        Episode.objects.create(number='003', title='Episode 3')
        Episode.objects.create(number='004', title='Episode 4')
        Episode.objects.create(number='005', title='Episode 5')
        Episode.objects.create(number='006', title='Episode 6')
        Episode.objects.create(number='007', title='Episode 7')
        Episode.objects.create(number='008', title='Episode 8')
        Episode.objects.create(number='009', title='Episode 9')
        Episode.objects.create(number='010', title='Episode 10')
        Episode.objects.create(number='011', title='Episode 11')
        Episode.objects.create(number='012', title='Episode 12')
        Episode.objects.create(number='013', title='Episode 13')


    def test_retrieve_episode_list(self):
        """
        Ensures that the active episode list is successfully pulled from database.
        """

        episode_list = repo.get_episodes()
        self.assertEqual(len(episode_list), 12)


    def test_retrieve_episode_list_with_take(self):
        """
        Ensures that a specified number most-recent active episodes
         are successfully pulled from database.
        """

        # take 6 episodes
        episode_list = repo.get_episodes(take=6)
        self.assertEqual(len(episode_list), 6)

        # take 9 episodes
        episode_list = repo.get_episodes(take=9)
        self.assertEqual(len(episode_list), 9)

        # ensure most recent episode is first in the list of returned episodes
        self.assertEqual(episode_list[0]['number'], '013')


    def test_get_episode_by_number(self):
        """
        Ensures that the application successfully returns an episode
         when provided a corresponding episode number.
        """

        episode = repo.get_episode_by_number('004')
        self.assertEqual('004', episode['number'])


    def test_episode_search(self):
        """
        Ensures that the application will return a list of Active episode
         data if an episode's number, title, or content contains
         a user-inputted search term.
        """

        # will include Episode 10, Episode 11, Episode 12 and Episode 13.
        # will not include Episode 1 because it is not Active.
        episodes = repo.search('Episode 1')
        self.assertEqual(4, len(episodes))

        # will return empty list
        episodes = repo.search('Gobble gobble')
        self.assertEqual(0, len(episodes))


    def test_get_episode_by_number_not_found(self):
        """
        Ensures that if a supplied episode number does not exist,
         the application returns None.
        """

        episode = repo.get_episode_by_number('999')
        self.assertEqual(None, episode)

    def test_get_episode_by_number_not_active(self):
        """
        Ensures that if a supplied episode number exists,
         but the episode is not active, the application returns None.
        """

        episode = repo.get_episode_by_number('001')
        self.assertEqual(None, episode)

    def test_episode_model_str_method(self):
        """
        Ensures that the __str__ method functions as intended.
        """

        episode = Episode.objects.filter(number='005').get()
        self.assertEqual('005- Episode 5', episode.__str__())


class EpisodeConfigTestCase(TestCase):
    def test_app_config(self):
        self.assertEqual(EpisodesConfig.name, 'episodes')
        self.assertEqual(apps.get_app_config('episodes').name, 'episodes')