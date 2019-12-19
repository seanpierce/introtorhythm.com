from django.contrib import admin

from .models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('number','title','content')
    list_filter = ('active','created_at')

admin.site.register(Episode, EpisodeAdmin)
