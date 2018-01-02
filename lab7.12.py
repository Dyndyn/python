#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

s = input("enter the string ")


def remove_spaces(s):
    return re.sub('( )( )+', r'\1', s).strip()


print(remove_spaces(s))

