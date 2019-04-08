"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import timeit
import cProfile
from random import randint

n = 1000000

n_list = [randint(-100, 100) for _ in range(0, n + 1, 1)]

def find_max_negative(n_list):
    # print(n_list)
    abs_min = abs(min(n_list))
    find_number = 0
    find_number_index = 0

    for index, number in enumerate(n_list):
        abs_number = abs(number)
        if number < 0 and abs_number < abs_min:
            abs_min = abs_number
            find_number = number
            find_number_index = index

    # print(find_number)
    # print(find_number_index)

"""
Данные - массив размером n. Цикл проходит по всем n значениям массива. 
Колчисество операций для одной итерации:
1 Проверка if
2 number < 0
3 abs(number)
4 abs(number) < abs_min
5 abs(number)
6 abs_min = abs(number)
7 find_number = number
8 find_number_index = index
Операции вне цикла:
1 min(n_list)
2 abs(min(n_list))
3 abs_min = abs(min(n_list))
4 find_number = 0
5 find_number_index = 0
Сложность min(n_list) - n
Итого сложность алгоритма: 8*n + n + 4 = 9n + 4 или O(n)
Улучшение:
abs(number) выполнить 2 раз вместо трудоемкой операции присваивания
Результат выпонения двух вариантов 0.389 seconds против 0.563 seconds
"""


def find_max_negative_improved(n_list):
    # print(n_list)
    abs_min = abs(min(n_list))
    find_number = 0
    find_number_index = 0

    for index, number in enumerate(n_list):
        if number < 0 and abs(number) < abs_min:
            abs_min = abs(number)
            find_number = number
            find_number_index = index

    # print(find_number)
    # print(find_number_index)

find_max_negative(n_list)
cProfile.run('find_max_negative(n_list)')

find_max_negative_improved(n_list)
cProfile.run('find_max_negative_improved(n_list)')
