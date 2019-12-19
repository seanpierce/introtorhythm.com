from .models import Content

class ContentRepository(object):
    """Access layer for reading and writing Content data."""

    @staticmethod
    def get_content_by_name(name):
        """Returns content data when provided a name alias."""
        content = Content.objects.filter(active=True, name__iexact=name).first()
        return {
            'id': content.id,
            'name': content.name,
            'info': content.info
        }