#!/usr/bin/python
#-*- coding: utf-8 -*-


s = input("enter the string? ")

def isPalindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

print (isPalindrome(s))


