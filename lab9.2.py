#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
number = input("Enter number (dot is delimiter): ")


def wording(number):
    digits = {
        0: 'нуль',
        1: 'одна',
        2: 'дві',
        3: 'три',
        4: 'чотири',
        5: 'п\'ять',
        6: 'шість',
        7: 'сім',
        8: 'вісім',
        9: 'дев\'ять',
        10: 'десять',
        11: 'одинадцять',
        12: 'дванадцять',
        13: 'тринадцять',
        14: 'чотирнадцять',
        15: 'п\'ятнадцять',
        16: 'шістнадцять',
        17: 'сімнадцять',
        18: 'вісімнадцять',
        19: 'дев\'ятнадцять'
    }

    dozens = {
        2: 'двадцять',
        3: 'тридцять',
        4: 'сорок',
        5: 'п\'ятдесят',
        6: 'шістдесят',
        7: 'сімдесят',
        8: 'вісімдесят',
        9: 'дев\'яносто'
    }

    hundreds = {
        1: 'сто',
        2: 'двісті',
        3: 'триста',
        4: 'чотириста',
        5: 'п\'ятсот',
        6: 'шістсот',
        7: 'сімсот',
        8: 'вісімсот',
        9: 'дев\'ятсот'
    }

    strnum = str(number)
    if number < 20:
        return digits[number]
    elif number < 100:
        if strnum[-1] == '0':
            return dozens[int(strnum[0])]
        else:
            return dozens[int(strnum[0])] + " " + wording(int(strnum[1]))
    else:
        if strnum[1:3] == '00':
            return hundreds[int(strnum[0])]
        else:
            return hundreds[int(strnum[0])] + " " + wording(int(strnum[1:3]))




def splitByThousands(inputNum):
    arr = inputNum.split('.')
    if len(arr[1]) == 1:
        arr[1] = arr[1] + '0'
    cent = int(arr[1])
    num = int(arr[0])
    arrThousands = []
    arrThousands.append(cent)
    while num != 0:
        arrThousands.append(int(num % 1000))
        num = int(num/1000)
    return arrThousands

def main(number):

    names_of_numbers = {
        0: ['копійка', 'копійки', 'копійок'],#1, 2 3 4, 5 6 7 8 9 10 - 20
        1: ['гривня', 'гривні', 'гривень'],
        2: ['тисяча', 'тисячі', 'тисяч'],
        3: ['мільйон', 'мільйони', 'мільйонів'],
        4: ['мільярд', 'мільярди', 'мільярдів'],
    }

    arr = splitByThousands(number)
    result = ''

    for i in reversed(range(len(arr))):
        result = result + " " + wording(arr[i])
        strnum = str(arr[i])
        while len(strnum) < 3:
            strnum = '0' + strnum

        if re.match(r'.[^1]1', strnum):
            result = result + " " + names_of_numbers[i][0]
        elif re.match(r'.[^1][234]', strnum):
            result = result + " " + names_of_numbers[i][1]
        else:
            result = result + " " + names_of_numbers[i][2]
    return result.strip()

print(main(number))
