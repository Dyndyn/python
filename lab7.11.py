#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
import collections
s = input("enter the string ")


def smallest_len(s):
    words = re.sub("[^\w]", " ", s).split()
    map = dict()
    for word in words:
        if len(word) in map:
            map[len(word)] = map[len(word)] + " " + word
        else:
            map[len(word)] = word
    map = collections.OrderedDict(sorted(map.items()))
    return " ".join(map.values())


print(smallest_len(s))