from django.contrib import admin
from .models import Show

class ShowAdmin(admin.ModelAdmin):
    search_fields = ['title', 'info']
    list_filter = ['active']
    list_display = ['title', 'date', 'start_time']
    actions = ['mark_shows_active', 'mark_shows_inactive']

    def mark_shows_active(self, request, queryset):
        queryset.update(active=True)

    def mark_shows_inactive(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Show, ShowAdmin)