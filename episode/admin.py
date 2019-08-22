from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('number','title','content')
    list_filter = ('active','created_at')

admin.site.register(Episode, EpisodeAdmin)

# Customize admin
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = 'Intro To Rhythm'
admin.site.site_header = 'Intro To Rhythm'
admin.site.index_title = 'Admin Dashboard'