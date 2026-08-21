from django.contrib import admin

from .models import About, Connections, MarqueeText

#region About

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """
        Ensure only one record can be added.
        """
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        """
        Ensure record can not be deleted.
        """
        return False
    
admin.site.register(About, AboutAdmin)

# endregion

#region Connections

class ConnectionsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """
        Ensure only one record can be added.
        """
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        """
        Ensure record can not be deleted.
        """
        return False
    
admin.site.register(Connections, ConnectionsAdmin)

# endregion

#region MarqueeText

class MarqueeTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """
        Ensure only one record can be added.
        """
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        """
        Ensure record can not be deleted.
        """
        return False
    
admin.site.register(MarqueeText, MarqueeTextAdmin)

# endregion