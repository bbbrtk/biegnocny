from django import template

register = template.Library()

@register.tag(name='increment')
def incrementing(value,argument):
    argument=argument+1
    return argument
