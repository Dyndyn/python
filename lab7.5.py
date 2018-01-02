#!/usr/bin/python
#-*- coding: utf-8 -*-

s = input("enter the string? ")


def count(s):
    num = 0
    letters = ['a', 'o', 'u', 'i', 'e', 'y']
    for letter in s:
        if letter in letters:
            num += 1
    return num


print ("result = {}".format(count(s)))


