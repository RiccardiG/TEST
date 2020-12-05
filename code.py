#!/usr/bin/python

input('Hello There')


def swap(a, b):
    a, b = b, a
    return a, b


a = int(input("Choose a value"))
b = int(input("Choose another value"))
a, b = swap(a, b)
print(a, b, 'Have been swapped')
