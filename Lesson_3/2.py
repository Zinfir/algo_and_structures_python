"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint, random

index_list = []

n_list = [randint(0, 100) for _ in range(0, 21, 1)]

for index, number in enumerate(n_list):
    if number % 2 == 0:
        index_list.append(index)

print(n_list)

print(index_list)
