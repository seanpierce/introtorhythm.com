from django.test import TestCase

class IntroToRhythmTestCase(TestCase):

    def test_index_route(self):
        response = self.client.get('/', follow=True)
        self.assertTemplateUsed(response, 'app.html')

    def test_episodes_route(self):
        response = self.client.get('/episodes', follow=True)
        self.assertTemplateUsed(response, 'app.html')

    def test_episode_route(self):
        response = self.client.get('/episodes/002', follow=True)
        self.assertTemplateUsed(response, 'app.html')

    def test_unsubscribe_route(self):
        response = self.client.get('/unsubscribe', follow=True)
        self.assertTemplateUsed(response, 'app.html')