#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.


def permutation(s):
    """
    Перестановка
    """
    if len(s) == 1:
        return [s]

    perm_list = []
    for a in s:
        elements = [x for x in s if x != a]
        z = permutation(elements)

        for t in z:
            perm_list.append([a] + t)

    return perm_list


def main():
    """
    Главная функция программы
    """
    n = int(input("Введите число: "))

    arr = list(range(1, n + 1))

    for line in permutation(arr):
        print(line)


if __name__ == '__main__':
    main()
