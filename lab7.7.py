#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

s = input("enter the string? ")


def to_snake_case(s):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def to_camel_case(s):
    first, *rest = s.split('_')
    return first + ''.join(word.capitalize() for word in rest)


print(to_snake_case(s))
print(to_camel_case(s))

