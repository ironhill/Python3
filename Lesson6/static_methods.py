#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.siblings = []

    def print(self):
        print(self.name, 'is', self.age)
        print('Mys siblings')
        for sibling in self.siblings:
            print(sibling.name)

    @staticmethod
    def add_siblings(first, second):
        siblings.append(float)
        siblings.append(second)


john = Person('John', 25)
mary = Person('Mary', 22)

john.print()
mary.print()
