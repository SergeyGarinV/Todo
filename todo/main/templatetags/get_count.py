from django.template.defaulttags import register


@register.filter
def get_count(value):
    return list(range(7 - len(value)))
