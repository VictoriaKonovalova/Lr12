#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.

def permutation(s):
    """
        Перестановка чисел
    """
    if len(s) == 1:
        return [s]  # терминальная ветвь
    else:
        a = s[0]  # первый элемент списка
        p = permutation(s[1:])  # все перестановки хвоста
        r = []
        for pp in p:  # вставляем a в каждую возможную позицию каждой перестановки хвоста
            for i in range(len(pp)):
                tmp = pp[0:i] + [a] + pp[i:]
                r.append(tmp)
            r.append(pp)
        return r


def main():
    """
    Главная функция программы
    """
    n = int(input("n="))
    print(permutation([i for i in range(1, n + 1)]))


if __name__ == '__main__':
    main()
