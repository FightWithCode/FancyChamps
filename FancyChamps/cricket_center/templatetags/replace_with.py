from django import template


register = template.Library()


@register.filter
def convert_to_underscore(value):
    return value.title().replace(" ", "_")


@register.filter
def convert_to_space(value):
    return value.title().replace("_", " ")


@register.filter
def get_id_one(value):
    return str(value) + "_1"


@register.filter
def get_id_two(value):
    return str(value) + "_2"
