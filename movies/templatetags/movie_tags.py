from django import template

register = template.Library()


@register.filter
def in_number(things, number):
    return things.filter(number=number).first().iframe_link


@register.filter
def last_number(things):
    return things.series.all().order_by("number").last()
