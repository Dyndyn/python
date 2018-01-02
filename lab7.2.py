#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

s = input("enter the string? ")

def isPalindrome(string):
    string = re.sub(r'\W+', '', string).lower()
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

print (isPalindrome(s))


