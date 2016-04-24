#!/usr/bin/env python
# -*- coding: utf-8 -*-


def print_hello(name, *, count):
    for i in range(count):
        print("Hello, " + name + '!')

print_hello('Ihor', count=3)
print_hello('Python', count=3)
