#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def speed_in_time(a_value, b_value, time_value):
    return round(a_value * (math.exp(-(time_value - b_value) ** 2)), 3)


def path(a_value, b_value, time_1, time_2):
    return round(((a_value * math.sqrt(math.pi)) * (math.erf(b_value - time_1) - math.erf(b_value - time_2)) / 2), 3)


a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
t1 = float(input("Enter t1 value: "))
t2 = float(input("Enter t2 value: "))

print("v1=", speed_in_time(a, b, t1))
print("v2=", speed_in_time(a, b, t2))
print("S=", path(a, b, t1, t2))

