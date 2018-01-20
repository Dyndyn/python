#!/usr/bin/python
#-*- coding: utf-8 -*-
arabic = int(input("Enter arabic number: "))
roman = str(input("Enter roman number: "))


def toRomanNumber(arabicNumber):
    if arabicNumber > 3999:
        raise Exception('Number cannot be greater than 3999')

    digitsSymbols = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dozensSymbols = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundredsSymbols = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousandsSymbols = ["", "M", "MM", "MMM"]

    thousands = thousandsSymbols[arabicNumber // 1000]
    hundreds = hundredsSymbols[arabicNumber // 100 % 10]
    dozens = dozensSymbols[arabicNumber // 10 % 10]
    digits = digitsSymbols[arabicNumber % 10]

    return thousands + hundreds + dozens + digits


def toArabicNumber(romanNumber):
    romanNumber = romanNumber.upper()

    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    arabicNumber = 0

    count = len(romanNumber)
    for i in range(count):
        if i < count - 1 and dictionary[romanNumber[i]] < dictionary[romanNumber[i + 1]]:
            continue
        elif i > 0 and dictionary[romanNumber[i - 1]] < dictionary[romanNumber[i]]:
            arabicNumber += dictionary[romanNumber[i]] - dictionary[romanNumber[i - 1]]
        else:
            arabicNumber += dictionary[romanNumber[i]]

    return arabicNumber


print('{} = {}'.format(arabic, toRomanNumber(arabic)))
print('{} = {}'.format(roman, toArabicNumber(roman)))