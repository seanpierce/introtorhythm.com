import json 

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
        Episode.objects.create(number='013', title='Episode 13')

    def test_retrieve_episode_list(self):
        """Ensures that the active episode list is successfully pulled from database"""
        episode_list = repo.get_latest_episode_list()
        self.assertEqual(len(episode_list), 10)

    def test_retrieve_episode_list_by_number_not_in_most_recent_ten(self):
        """Ensures that the active episode list is successfully pulled from database
        begining at the provided episode.
        """
        episode_list = repo.get_episode_list_by_number('002')
        self.assertEqual(len(episode_list), 10)

    def test_retrieve_episode_list_by_number_in_most_recent_ten(self):
        """Ensures that the most recent, active episode list is successfully pulled from database"""
        episode_list = repo.get_episode_list_by_number('008')
        self.assertEqual(len(episode_list), 10)

    def test_get_current_episode(self):
        """Ensures that the current episode is successfully pulled from the database"""
        current_episode = repo.get_current_episode()
        self.assertEqual('013', current_episode['number'])

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

    def test_episode_model_str_method(self):
        """Ensures that the __str__ method functions as intended."""
        ep = Episode.objects.filter(number='005').get()
        self.assertEqual('005- Episode 5', ep.__str__())

    def test_index_route(self):
        response = self.client.get('/', follow=True)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_route_data(self):
        response = self.client.get('/', follow=True)
        data = json.loads(response.context['data'])
        self.assertEqual('013', data['current_episode']['number'])

    def test_episode_route(self):
        response = self.client.get('/002', follow=True)
        self.assertTemplateUsed(response, 'index.html')

    def test_episode_not_found_route(self):
        response = self.client.get('999', follow=True)
        self.assertTemplateUsed(response, '404.html')