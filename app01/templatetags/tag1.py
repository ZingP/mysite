#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/12

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def tag_add_3_no(v1, v2, v3):
    return v1 + v2 + v3

@register.simple_tag
def my_input(name):
    result = "<h1> %s </h1>" % name
    # mark_safe 会让html标签合法
    return mark_safe(result)

