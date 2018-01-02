#!/usr/bin/python
#-*- coding: utf-8 -*-

s = input("enter the string? ")


def print_in_frame(s):
    frame = "*" * (len(s) + 4)
    result = frame + "\n* {} *\n" + frame
    print(result.format(s))

print_in_frame(s)


