#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = 0
while n <= 10:
    n += 1
    if 5 < n <= 8:
        continue
    print('New number:')
    print(n)
    print()
