from content.models import BackgroundImage, SiteInfo, LiveCallout

class ContentRepository(object):
    """Access layer for reading and writing Content data."""

    @staticmethod
    def get_live_callout():
        return LiveCallout.objects.values('content', 'active').first()


    @staticmethod
    def get_site_info():
        return SiteInfo.objects.values('info').first()


    @staticmethod
    def get_background_image():
        return BackgroundImage.objects.values('image', 'active').first()