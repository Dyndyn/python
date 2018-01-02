#!/usr/bin/python
#-*- coding: utf-8 -*-

s = input("What's the string? ")
offset = int(input("What's the offset? "))

def shift(string, offset):
    return string[offset:] + string[:offset]
print ("result = {}".format(shift(s, offset)))


