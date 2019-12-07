from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import Content, Image


class ContentAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields

admin.site.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj is None:
            return "Not available"
        else:
            return format_html('<img src="{}" width="150px" />'.format(obj.image.url))

    image_tag.short_description = 'Preview'

    list_display = ['image_tag','filename',]
    list_display_links = ['image_tag','filename',]
    readonly_fields = ['image_tag',]

admin.site.register(Image, ImageAdmin)