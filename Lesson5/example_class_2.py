#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Article:
    def __init__(self, author, tittle, text, reviews=None):
        self.author = author
        self.tittle = tittle
        self.text = text
        self.reviews = reviews

    def add_review(self, review):
        pass


class Review:
    def __init__(self, author, rate, comment):
        self.author = author
        self.rate = rate
        self.comment = comment

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(self.name, 'is', self.age)