from django.template.defaulttags import register
from todo.settings import DIV_COUNT

@register.filter
def get_count(value):
    return range(DIV_COUNT - len(value))
