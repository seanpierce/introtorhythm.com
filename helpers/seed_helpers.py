import os
import requests
from faker import Faker


def get_image_file() -> bytes:
    """
    Generates an image using Faker.
    """

    fake = Faker()
    url = fake.image_url()
    response = requests.get(url)
    return response.content


def get_audio_file():
    filepath = 'assets/placeholder_media/audio.mp3'
    abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', filepath))
    return open(os.path.abspath(abs_path))