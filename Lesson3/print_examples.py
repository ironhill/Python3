#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

print(1, 2, 3, sep=' ', end='\n==============\n')

for i in range(1, 11):
    print(i, end=' ', flush=True)
    time.sleep(1)

print()
