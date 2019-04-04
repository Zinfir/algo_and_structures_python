"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

n_list = [randint(0, 100) for _ in range(0, 11, 1)]
print('Изначальный массив: ', n_list)

n_max = max(n_list)
n_min = min(n_list)
max_index = n_list.index(n_max)
min_index = n_list.index(n_min)
sum = 0

if min_index < max_index:
    for number in n_list[min_index + 1:max_index]:
        sum += number
    print('Срез между мин и мах элементами: ', n_list[min_index + 1:max_index])
else:
    for number in n_list[max_index + 1:min_index]:
        sum += number
    print('Срез между мин и мах элементами: ', n_list[max_index + 1:min_index])

print('Сумма: ', sum)