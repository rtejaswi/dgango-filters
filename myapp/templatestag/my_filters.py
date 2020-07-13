from django import template
from django.template.defaultfilters import stringfilter
#from django.utils.safestring import SafeString

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    return value.replace(arg, '')

# register.filter('cut', cut)

@register.filter
@stringfilter
def title(value):
    return value.title()

# @register.filter(is_safe = True)
# def myfilter(value):
#     return value
