"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

while True:
    try:
        n = int(input('Введите число n: '))
        break
    except ValueError:
        print('Введено некорректное значение')

def f(n):
    return n * (n + 1) / 2

def sum_n(n):
    count = n
    sum = 0
    tmp = 0
    while count:
        tmp += 1
        sum += tmp
        count -= 1
    return sum

if sum_n(n) == f(n):
    print('1+2+...+n = n(n+1)/2 выполняется для n = {}: {}={}'.format(n, sum_n(n), f(n)))
else:
    print('1+2+...+n = n(n+1)/2 не выполняется для n = {}: {}={}'.format(n, sum_n(n), f(n)))
