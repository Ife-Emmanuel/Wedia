from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.register(Entry)

@admin.register(Topic)
class TopicModel(admin.ModelAdmin):
    list_filter = ('text', 'owner')
    list_display = ('text', 'owner')
