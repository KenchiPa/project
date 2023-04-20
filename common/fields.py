from django.db import models
from django.utils.html import mark_safe
from markdown import markdown
from config.settings import MARKDOWN_EXTENSIONS

class MarkdownField(models.TextField):
    """
    A TextField which stores markdown text and renders it as HTML using
    the python-markdown library.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return value

    def render(self, value):
        """
        Renders the field's markdown text as HTML.
        """
        return mark_safe(markdown(value, extensions=MARKDOWN_EXTENSIONS))