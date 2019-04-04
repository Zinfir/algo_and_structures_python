# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

array = [[randint(0, 100) for _ in range(0, 4, 1)] for _ in range(0, 4, 1)]

print('Изначальный массив:')
for row in array:
    print(row)

def transpose(array):
    return [[ array[row][col] for row in range(0, 4) ] for col in range(0, 4) ]

array_t = transpose(array)

print()
print('Транспонированный массив:')
for row in array_t:
    print(row)

min_list = []

for row in array_t:
    min_list.append(min(row))

print()
print('Список мин элементов столбцов: ', min_list)

max_min = max(min_list)

print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max_min)
