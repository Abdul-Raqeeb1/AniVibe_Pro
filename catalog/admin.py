from django.contrib import admin
from .models import Show, StreamingPlatform, AffilliateLink


class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_type', 'release_date', 'rating')
    list_filter = ('show_type',) 
    search_fields = ('title',) 

admin.site.register(Show, ShowAdmin)
admin.site.register(StreamingPlatform)
admin.site.register(AffilliateLink)