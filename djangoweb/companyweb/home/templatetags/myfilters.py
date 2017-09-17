# coding=utf-8
from django import template
register=template.Library()
# 注册
@register.filter
def flow(value,arg1):
    diviser,reminder= arg1.split(',')

    diviser =int(diviser)
    reminder =int(reminder)

    if value % diviser==reminder:
        return True
    return False