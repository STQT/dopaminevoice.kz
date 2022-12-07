from django import template

register = template.Library()


@register.filter(name="func_floor_division")
def func_floor_division(num, val):
    if num:
        floor_division = num // val
        return floor_division
    else:
        return None
