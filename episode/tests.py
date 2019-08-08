from django.test import TestCase

from .models import Episode
from .repository import EpisodeRepository as repo

class EpisodeTestCase(TestCase):
    def setUp(self):
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

    def test_retrieve_episode_list(self):
        """Ensures that the active episode list is successfully pulled from database"""
        episode_list = repo.get_episode_list('00000')
        self.assertEqual(len(episode_list), 10)

    def test_get_current_episode(self):
        """Ensures that the current episode is successfully pulled from the database"""
        current_episode = repo.get_current_episode()
        self.assertEqual('012', current_episode['number'])

    def test_get_current_episode_by_number(self):
        """Ensures that the current episode is successfully fetched given an episode number"""
        current_episode = repo.get_current_episode('002')
        self.assertEqual('002', current_episode['number'])

    def test_get_current_episode_by_number_not_found(self):
        """Ensures that if a supplied episode number that does not exist returns None."""
        current_episode = repo.get_current_episode('999')
        self.assertEqual(None, current_episode)

    def test_get_current_episode_by_number_not_active(self):
        """Ensures that if a supplied episode number exists, but is not active, returns None."""
        current_episode = repo.get_current_episode('001')
        self.assertEqual(None, current_episode)

    def test_return_false_if_item_is_not_in_most_recent_ten_episodes(self):
        """Ensures that the application knows wether or not an episode is in the most recent ten episodes given the episode number."""
        self.assertEqual(False, repo.check_if_episode_in_most_recent_ten('002'))

    def test_return_true_if_item_is_in_most_recent_ten_episodes(self):
        """Ensures that the application knows wether or not an episode is in the most recent ten episodes given the episode number."""
        self.assertEqual(True, repo.check_if_episode_in_most_recent_ten('008'))