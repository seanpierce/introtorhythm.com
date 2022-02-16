from django.contrib import admin

from .models import Show

class ShowAdmin(admin.ModelAdmin):
    search_fields = ['title', 'info']
    list_filter = ['active']
    list_display = ['title', 'date', 'start_time']
    list_filter = ['active']

admin.site.register(Show, ShowAdmin)