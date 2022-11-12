from django import template

register = template.Library()


@register.filter
def last_number(things):
    return things.series.all().order_by("number")
