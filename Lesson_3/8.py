"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

array = [[] for _ in range(0, 4, 1)]

for index, row in enumerate(array):
    print('Ряд {}:'.format(index + 1))
    for number in range(0, 4, 1):
        row.append(int(input('Введите число: ')))
    row.append(0)

for row in array:
    for number in row[0:4]:
        row[4] += number

for row in array:
    print(row)
