from django.contrib import admin

from .models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_per_page = 10

  
admin.site.register(Episode, EpisodeAdmin)