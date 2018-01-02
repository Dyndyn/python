#!/usr/bin/python
#-*- coding: utf-8 -*-
s = input("enter the string ")


def is_lucky(s):
    if not s.isdigit(): return False
    first = s[:len(s)//2]
    second = s[-(len(s)//2):]
    return sum(int(x) for x in first) == sum(int(x) for x in second)


print(is_lucky(s))