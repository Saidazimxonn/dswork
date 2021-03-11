from django import template

register = template.Library()

@register.filter(name='to_int')
def to_int(val):
    try:
        return int(val)
    except:
        return val