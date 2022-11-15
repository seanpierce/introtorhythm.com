from content.models.content import SiteInfo, LiveCallout
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Seeding content data...')
        run()
        self.stdout.write('Content data complete!')


def run():
    """
    Creates single instances of models if they do not already exist.
    """
    
    if not LiveCallout.objects.exists():
        LiveCallout.objects.create()

    if not SiteInfo.objects.exists():
        SiteInfo.objects.create()