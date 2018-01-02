#!/usr/bin/python
#-*- coding: utf-8 -*-

s = input("What's the string? ")

def encrypt(s):
    from string import ascii_letters
    result = str()
    for c in s:
        if c == 'z': result += 'a'
        elif c == 'Z': result += 'A'
        elif c in ascii_letters:
            result = result + (ascii_letters[(ascii_letters.index(c) + 1) % len(ascii_letters)])
        else:
            result += c
    return result


print ("result = {}".format(encrypt(s)))


