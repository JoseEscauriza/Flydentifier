from django import template

register = template.Library()


@register.filter
def staff_filter(value):
    if value:
        return 'Yes'
    else:
        return 'No'
