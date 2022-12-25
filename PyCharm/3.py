# -*- coding: utf-8 -*-
# Итеративная версия

import timeit


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    r_fib = fib(15)
    r_factorial = factorial(15)

    print("Итеративная функция factorial: ")
    print(timeit.timeit("r_factorial", setup="from __main__ import r_factorial"))
    print("Итеративная функция fib: ")
    print(timeit.timeit("r_fib", setup="from __main__ import r_fib"))