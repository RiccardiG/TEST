#!/usr/bin/python

from functions.function_sum import *

# input('Hello There')


def swap(a, b):
    a, b = b, a
    return a, b


# a = int(input("Choose a value"))
# b = int(input("Choose another value"))
# a, b = swap(a, b)
# print(a, b, 'Have been swapped')


def main():
    print(function_sum(1, 2, 2, 3, 5))
    print("Hello")


if __name__ == '__main__':
    main()
