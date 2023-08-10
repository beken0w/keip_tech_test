from django.utils.html import format_html
from django.forms import widgets


class ImagePreviewWidget(widgets.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value and hasattr(value, 'url'):
            return format_html(
                '<div style="margin-bottom: 10px;"><img src="{}" alt="Image" style="max-height: 150px;"></div>',
                value.url,
            )
        return super().render(name, value, attrs, renderer)
    