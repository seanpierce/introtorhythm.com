import datetime
from .helpers import TIMES
from django.contrib import admin
from django.utils.encoding import force_text
from django.utils.html import format_html
from .models import Show, LiveRecording

class UpcomingFilter(admin.SimpleListFilter):
    title = 'Upcoming'
    parameter_name = 'upcoming'
    default_value= 'Upcoming'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Upcoming', 'Upcoming'),
            ('Past', 'Past'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        # Compare the requested value (either 'Upcoming' or 'Past')
        # to decide how to filter the queryset.

        if self.value() == None:
            self.used_parameters[self.parameter_name] = 'Upcoming'

        if self.value() == 'Upcoming':
            return queryset.filter(
                date__gte = datetime.date.today()
            )
        if self.value() == 'Past':
            return queryset.filter(
                date__lte = datetime.date.today()
            )

    def choices(self, changelist):
        """
        Override to remiove the 'All' option for this filter.
        """

        yield {
            'selected': self.value() is None,
            'query_string': changelist.get_query_string({}, [self.parameter_name]),
        }
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == force_text(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }


class UpcomingShowAdmin(admin.ModelAdmin):
    search_fields = ['title', 'info']
    list_filter = [UpcomingFilter, 'active']
    list_display = ['title', 'date', 'start_time', 'get_formatted_end_time', 'image_tag']
    actions = ['mark_shows_active', 'mark_shows_inactive']
    exclude = ['start_date_time', 'end_date_time', 'image_tag']

    def mark_shows_active(self, request, queryset):
        queryset.update(active=True)

    def mark_shows_inactive(self, request, queryset):
        queryset.update(active=False)

    def get_formatted_end_time(self, obj):
        """
        Returns the hour of the end_date_time field.
        Value is formatted using the TIMES helper.
        ex: if the hour is 18, field would show 6 pm.
        """
        return TIMES[obj.end_date_time.hour][1]

    get_formatted_end_time.short_description = 'End Time'

    def image_tag(self, obj):
        img_html = """
            <img src="{}" 
                onclick="window.open('{}', '_blank')"
                style="cursor:pointer;max-height:150px;max-width:150px;" />
        """
        try:
            if obj is not None and obj.show_image:
                return format_html(img_html.format(obj.show_image.url, obj.show_image.url))
            else:
                return 'No image available'
        except:
            return 'No image available'

    image_tag.short_description = 'Image'


class LiveRecordingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'info']
    list_display = ['title', 'start_date_time', 'image_tag']
    # actions = ['publish']
    exclude = ['start_date_time', 'image_tag']

    def image_tag(self, obj):
        img_html = """
            <img src="{}" 
                onclick="window.open('{}', '_blank')"
                style="cursor:pointer;max-height:150px;max-width:150px;" />
        """
        try:
            if obj is not None and obj.show_image:
                return format_html(img_html.format(obj.show_image.url, obj.show_image.url))
            else:
                return 'No image available'
        except:
            return 'No image available'

    image_tag.short_description = 'Image'


admin.site.register(Show, UpcomingShowAdmin)
admin.site.register(LiveRecording, LiveRecordingAdmin)