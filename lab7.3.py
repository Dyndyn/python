#!/usr/bin/python
#-*- coding: utf-8 -*-

s = input("What's the string? ")

def isValid(s):
    OPENING_BRACKETS = {"{", "[", "("}
    CLOSING_BRACKETS = {"]", "}", ")"}
    BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}
    stack = []
    for bracket in s:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif bracket in CLOSING_BRACKETS:
            if not stack: return False
            last = stack.pop()
            if BRACKETS_MAP.get(bracket) != last:
                return False

    return not stack


print ("result = {}".format(isValid(s)))


