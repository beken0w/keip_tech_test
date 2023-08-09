from django.contrib import admin

from news.models import Post

EMPTY_DATA = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'date', 'title', 'text')
    list_editable = ('date', 'title', 'text')
    search_fields = ('category', 'date', 'title', 'text')
    list_filter = ('category', 'date', 'title', 'text')
    empty_value_display = EMPTY_DATA
