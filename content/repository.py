from .models import Content, BackgroundImage

class ContentRepository(object):
    """Access layer for reading and writing Content data."""

    @staticmethod
    def get_content_by_name(name):
        """Returns content data when provided a name alias."""
        content = Content.objects.filter(active=True, name__iexact=name).first()

        if content is None:
            return None

        return {
            'id': content.id,
            'name': content.name,
            'info': content.info,
            'active': content.active
        }


    @staticmethod
    def get_background_image():
        """Returns the background image url for th econfigured background image."""
        return BackgroundImage.objects.values('image', 'active').first()