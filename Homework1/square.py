#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import decimal

a = decimal(input("Enter a value: "))
b = decimal(input("Enter b value: "))
c = decimal(input("Enter c value: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("No solution in real numbers")
elif D == 0:
    print("X1, X2 = ", -b / (2 * a))
else:
    print("X1 = ", (-b - D ** 0.5) / 2 * a, "X2 =", (-b + D ** 0.5) / 2 * a)
