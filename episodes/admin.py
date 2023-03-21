from django.contrib import admin
from .models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['number','title','content']
    list_filter = ['active','featured','created_at']
    list_display = ['active', 'number', 'title', 'expiration_date']
    list_display_links = ['title']
    actions = ['mark_episodes_active', 'mark_episodes_inactive']
    exclude = ['expiration_date']


    def get_form(self, *args, **kwargs):
        help_texts = {
            'display_expiration_method': 'Determines the date that an episode will expire. Once expired, all data and associated media will be purged. Expiration date is dependent upon the values of the active and featured toggles.'
        }
        kwargs.update({'help_texts': help_texts})
        return super().get_form(*args, **kwargs)

    def display_expiration_method(self, obj):
        return obj.expiration_date

    readonly_fields=['display_expiration_method']

    display_expiration_method.short_description = 'Expiration'

    def mark_episodes_active(self, request, queryset):
        queryset.update(active=True)

    def mark_episodes_inactive(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Episode, EpisodeAdmin)
