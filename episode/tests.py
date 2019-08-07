from django.test import TestCase

from .models import Episode
from .repository import EpisodeRepository as repo

class EpisodeTestCase(TestCase):
    def setUp(self):
        Episode.objects.create(number='001', title='Episode 1', active=False)
        Episode.objects.create(number='002', title='Episode 2')
        Episode.objects.create(number='003', title='Episode 3')

    def test_retrieve_episode_list(self):
        """Ensures that the active episode list is successfully pulled from database"""
        episode_list = repo.get_episode_list()
        self.assertEqual(len(episode_list), 2)

    def test_get_current_episode(self):
        """Ensures that the current episode is successfully pulled from the database"""
        current_episode = repo.get_current_episode()
        self.assertEqual('003', current_episode['number'])

    def test_get_current_episode_by_number(self):
        """Ensures that the current episode is successfully fetched given an episode number"""
        current_episode = repo.get_current_episode('002')
        self.assertEqual('002', current_episode['number'])

    def test_get_current_episode_by_number_not_found(self):
        """Ensures that if a supplied episode number that does not exist returns None."""
        current_episode = repo.get_current_episode('004')
        self.assertEqual(None, current_episode)