from django.core.management.base import BaseCommand
from episodes.models import Episode
from episodes.services import EpisodesService
from faker import Faker
from helpers.seed_helpers import get_image_file, get_audio_file


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Seeding episode data...')
        run()
        self.stdout.write('Episode data complete!')


def run():
    """
    Scaffolds placeholder episode data.
    """

    for _ in range(1, 10):
        fake = Faker()
        episode = Episode()
        episode.title = fake.text(max_nb_chars=225)
        episode.number = EpisodesService.get_max_episode_number()
        episode.content = fake.sentences(nb=10)
        episode.tags = f"{fake.word()}, {fake.word()}"
        episode.image.save(f"{fake.word()}.png", get_image_file())
        episode.audio.save(f"{fake.word()}.mp3", get_audio_file())
        episode.save()
