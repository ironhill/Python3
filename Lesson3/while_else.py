#!/usr/bin/env python
# -*- coding: utf-8 -*-

attempt_left = 3

while attempt_left:
    password = input('Enter your password: ')
    if password == 'qwerty123':
        print('Access granted')
        break
    print('Incorrect password')
    attempt_left -= 1
    print('You have', attempt_left, 'attempt left!')
    print()
else:
    print("Access denied")
