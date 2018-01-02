#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
s = input("enter the string ")


def smallest_len(s):
    first, *rest = re.sub("[^\w]", " ", s).split()
    size = len(first)
    for word in rest:
        if len(word) < size:
            size = len(word)
    return size


print(smallest_len(s))