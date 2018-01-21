#!/usr/bin/python
#-*- coding: utf-8 -*-
import re


def read_in_chunks(file_object):
    while True:
        # data = file_object.read(chunk_size)
        data = file_object.readline();
        if not data:
            break
        yield data


f = open('2017_05_07_nginx.txt')
get = 0;
post = 0;
prog = re.compile(r'.* "(POST|GET).*" \d{3} (\d+) ".*')
for piece in read_in_chunks(f):
    m = prog.match(piece)
    print("{} {}".format(m.group(1), m.group(2)))
    if m.group(1) == "GET":
        get += int(m.group(2))
    else:
        post += int(m.group(2))

print("GET = {}, POST = {}".format(get, post))