#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
t1 = float(input("Enter t1 value: "))
t2 = float(input("Enter t2 value: "))

print("V1 in t1=", round(a * (math.exp(-(t1 - b) ** 2)), 3))
print("V1 in t1=", round(a * (math.exp(-(t2 - b) ** 2)), 3))
print("S=", round(((a * math.sqrt(math.pi)) * (math.erf(b - t1) - math.erf(b - t2)) / 2), 3))
