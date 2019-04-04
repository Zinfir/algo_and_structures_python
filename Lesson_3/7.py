"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

n_list = [randint(0, 100) for _ in range(0, 11, 1)]
print('Массив: ', n_list)

min_1 = n_list.pop(n_list.index(min(n_list)))
min_2 = n_list.pop(n_list.index(min(n_list)))

print('Первое мин число: ', min_1)
print('Второе мин число: ', min_2)