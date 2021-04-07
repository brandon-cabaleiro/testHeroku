# See the Django Admin documentaiton for the MANY options
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Tag, PhysicalLocation, Media, Person, RecordingSession
from .forms import TagForm, MediaForm

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm
    list_filter = ['name', 'created_at', 'updated_at']
    list_display = ['name']
    search_fields = ['name']

@admin.register(PhysicalLocation)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['created_at', 'updated_at']

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    form = MediaForm
    list_display = ['name', 'date_published', 'is_physical']
    list_filter = ['is_physical', 'date_published', 'file_extension', 'created_at', 'updated_at']
    readonly_fields = ['file_extension']
    autocomplete_fields = ['tags', 'physical_location']
    search_fields = ['name', 'description', 'file_extension', 'personnel__name', 'tags__name']
    filter_horizontal = ['related_media']
    formfield_overrides = {
        models.TextField: {'widget': Textarea},
    }

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    filter_horizontal = ['media', 'tags']

@admin.register(RecordingSession)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'date']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'location', 'date']
    filter_horizontal = ['personnel', 'media']
