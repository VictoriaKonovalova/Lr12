# -*- coding: utf-8 -*-
# Рекурсия с @lru_cache

from functools import lru_cache
import timeit


@lru_cache(maxsize=10)
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@lru_cache(maxsize=10)
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    r_fib = fib(15)
    r_factorial = factorial(15)

    print("Рекурсивная функция factorial с lru_cache:")
    print(timeit.timeit("r_factorial", setup="from __main__ import r_factorial"))
    print("Рекурсивная функция fib с lru_cache:")
    print(timeit.timeit("r_fib", setup="from __main__ import r_fib"))
