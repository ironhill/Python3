#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(self.name, 'is', self.age)

john = Person('John', 25)
mary = Person('MAry', 22)

john.print()
mary.print()
