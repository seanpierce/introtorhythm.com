from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import Content, BackgroundImage


class ContentAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields


class BackgroundImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj is None:
            return "Not available"
        else:
            return format_html('<img src="{}" width="150px" />'.format(obj.image.url))

    image_tag.short_description = 'Preview'

    list_display = ['image_tag', 'filename',]
    list_display_links = ['image_tag', 'filename',]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('image_tag',)
        return self.readonly_fields

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Content, ContentAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)