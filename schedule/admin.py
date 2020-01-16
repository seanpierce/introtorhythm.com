from django.contrib import admin

from .models import Show

class ShowAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['day', 'active']

admin.site.register(Show, ShowAdmin)