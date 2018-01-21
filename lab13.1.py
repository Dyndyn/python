#!/usr/bin/python
#-*- coding: utf-8 -*-
import abc
import decimal
import random


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def __str__(self) -> str:
        return "%s %.2f" % (self.name, self.salary)

    @abc.abstractmethod
    def calculate_salary(self) -> decimal.Decimal:
        return

    @abc.abstractmethod
    def calculate_taxes(self) -> decimal.Decimal:
        return

    def __gt__(self, other):
        if self.salary != other.salary:
            return self.salary > other.salary
        else:
            return self.name.__gt__(other.name)


class EmployeeWithHourlyPayment(Employee):
    def __init__(self, name, rate):
        self.name = name
        self.rate = decimal.Decimal(rate)
        self.income_tax = decimal.Decimal('0.18')
        self.military_duty = decimal.Decimal('0.015')
        self.calculate_salary()

    def calculate_salary(self, hours=decimal.Decimal(20.8)*decimal.Decimal(8)) -> decimal.Decimal:
        self.salary = decimal.Decimal(hours * self.rate).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
        return self.salary

    def calculate_taxes(self) -> decimal.Decimal:
        return (self.salary / (self.income_tax + self.military_duty + 1))\
                .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP) * \
               (self.income_tax + self.military_duty)

    def __str__(self) -> str:
        return "Hourly %s %.2f %.2f" % (self.name, self.salary, self.calculate_taxes())


class EmployeeWithMonthlyPayment(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = decimal.Decimal(salary)
        self.income_tax = decimal.Decimal('0.18')
        self.military_duty = decimal.Decimal('0.015')

    def calculate_salary(self) -> decimal.Decimal:
        return self.salary

    def calculate_taxes(self) -> decimal.Decimal:
        return (self.salary / (self.income_tax + self.military_duty + 1))\
                .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP) \
               * (self.income_tax + self.military_duty)

    def __str__(self) -> str:
        return "Monthly %s %.2f %.2f" % (self.name, self.salary, self.calculate_taxes())


class Entrepreneur(Employee):
    def __init__(self, name, rate):
        self.name = name
        self.rate = decimal.Decimal(rate)
        self.single_social_contribution = decimal.Decimal('704')
        self.single_tax = decimal.Decimal('0.05')
        self.calculate_salary()

    def calculate_salary(self, hours=decimal.Decimal(20.8)*decimal.Decimal(8)) -> decimal.Decimal:
        self.salary = decimal.Decimal(hours * self.rate)\
                          .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP) * decimal.Decimal('1.1')
        return self.salary

    def calculate_taxes(self) -> decimal.Decimal:
        return ((self.salary - self.single_social_contribution) / (self.single_tax + 1))\
                .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP) * \
                self.single_tax + self.single_social_contribution

    def __str__(self) -> str:
        return "Entrepreneur %s %.2f %.2f" % (self.name, self.salary, self.calculate_taxes())


class SelfEmployed(Employee):
    def __init__(self, name, rate):
        self.name = name
        self.rate = decimal.Decimal(rate)
        self.single_social_contribution = decimal.Decimal('704')
        self.income_tax = decimal.Decimal('0.18')
        self.military_duty = decimal.Decimal('0.015')
        self.calculate_salary()

    def calculate_salary(self, lines=decimal.Decimal(10000)) -> decimal.Decimal:
        self.salary = decimal.Decimal(lines * self.rate)\
                          .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
        return self.salary

    def calculate_taxes(self) -> decimal.Decimal:
        return ((self.salary - self.single_social_contribution) / (self.income_tax + self.military_duty + 1))\
                .quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP) * \
               (self.income_tax + self.military_duty) + self.single_social_contribution

    def __str__(self) -> str:
        return "SelfEmployed %s %.2f %.2f" % (self.name, self.salary, self.calculate_taxes())


employees = []
names = ['Вася', 'Роман', 'Андрій','Петро', 'Валентин','Йосип', 'Євген','Святослав', 'Олександр','Володимир', 'Михайло']
for i in range(3):
    employees.append(EmployeeWithHourlyPayment(names[random.randint(0, len(names)-1)], random.randint(80, 150)))

for i in range(3):
    employees.append(EmployeeWithMonthlyPayment(names[random.randint(0, len(names)-1)], random.randint(5000, 20000)))

for i in range(3):
    employees.append(Entrepreneur(names[random.randint(0, len(names)-1)], random.randint(80, 150)))

for i in range(3):
    employees.append(SelfEmployed(names[random.randint(0, len(names)-1)], random.uniform(0.5, 1.5)))

employees.sort()

print('\n'.join(map(str, employees)))