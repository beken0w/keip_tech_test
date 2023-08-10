from django.contrib import admin
from django.db import models
from news.widgets import ImagePreviewWidget
from news.models import News

EMPTY_DATA = '-пусто-'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'title', 'text')
    list_editable = ('date', 'title', 'text')
    search_fields = ('category', 'date', 'title', 'text')
    list_filter = ('category', 'date', 'title', 'text')
    formfield_overrides = {
        models.ImageField: {'widget': ImagePreviewWidget}
    }
    empty_value_display = EMPTY_DATA
