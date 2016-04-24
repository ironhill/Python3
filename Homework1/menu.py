#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Menu: \n1. Function\n2. Function\n3. Function\n")

entered_value = input("Make your choice: ")

if entered_value == '1' or entered_value == '2' or entered_value == '3':
    print("You choose: " + entered_value + " function")
else:
    print("Incorrect value! " + entered_value)