#!/usr/bin/env python
# -*- coding: utf-8 -*-

string_to_check = input("Input string: ")

if string_to_check:
    print("The string is empty...")
elif len(string_to_check) == 1:
    print("String length is:", len(string_to_check), "symbol")
else:
    print("String length is:", len(string_to_check), "symbols")
