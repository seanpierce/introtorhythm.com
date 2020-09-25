from django.contrib import admin

from .models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['number','title','content']
    list_filter = ['active','featured','created_at']
    list_display = ['active', 'number', 'title']
    list_display_links = ['title']
    actions = ['mark_episodes_active', 'mark_episodes_inactive']

    def mark_episodes_active(self, request, queryset):
        queryset.update(active=True)

    def mark_episodes_inactive(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Episode, EpisodeAdmin)
