from django.contrib import admin
from .models import  Event
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme_id', 'date', 'media_type')
    list_filter = ('theme_id', 'media_type', 'date')
    search_fields = ('title', 'description')
