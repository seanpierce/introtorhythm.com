import datetime
from django.contrib import admin
from django.utils.encoding import force_text
from .models import Show

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
    list_display = ['title', 'date', 'start_time']
    actions = ['mark_shows_active', 'mark_shows_inactive']
    exclude = ['start_date_time', 'end_date_time']

    def mark_shows_active(self, request, queryset):
        queryset.update(active=True)

    def mark_shows_inactive(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Show, UpcomingShowAdmin)