#!/usr/bin/env python
# -*- coding: utf-8 -*-

password = 'qwerty123'

pass_attempt = input("Please enter password: ")

if pass_attempt == password:
    print("Access was granted")
else:
    print("Access denied!")
