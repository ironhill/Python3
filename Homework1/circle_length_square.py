#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

radius = float(input("Enter circle radius: "))

print("Circle length:", round((2 * math.pi * radius), 2))
print("Circle square:", round((math.pi * (radius ** 2)), 2))
