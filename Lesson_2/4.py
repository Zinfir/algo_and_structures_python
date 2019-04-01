"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


try:
    n = int(input('Введите число n: '))
except ValueError:
    print('Введено некорректное значение')

def sum_n(n):
    count = 0
    sum = 0
    while count < n:
        if count % 2:
            sum += (0.5 ** count) * -1
            print((0.5 ** count) * -1)
        else:
            sum += 0.5 ** count
            print(0.5 ** count)
        count += 1
    return sum
print('sum = ', sum_n(n))