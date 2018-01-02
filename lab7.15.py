#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
import random


def pw_gen(size=8):
    chars_len = random.randint(size//2, size - 2);
    digits_len = size - chars_len - 1;

    password = list()
    password.extend(random.choice(string.ascii_letters) for _ in range(chars_len))
    password.extend(random.choice(string.digits) for _ in range(digits_len))
    password.append(random.choice(string.punctuation))
    random.shuffle(password)
    return "".join(password)

print(pw_gen(10))