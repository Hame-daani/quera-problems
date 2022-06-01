from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def fa_num(value: str):
    fa = "۰۱۲۳۴۵۶۷۸۹"
    res = value
    for c in value:
        if c.isnumeric():
            res = res.replace(c, fa[int(c)])
    return res
