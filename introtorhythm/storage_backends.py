from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'dev/media' if settings.DEBUG else 'media' 
    file_overwrite = False