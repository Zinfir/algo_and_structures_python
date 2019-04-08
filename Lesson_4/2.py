"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile

def is_simple(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    result = True
    for item in range(2, number, 1):
        if number % item == 0:
            result = False
        else:
            continue
    return result

def my_func(n):
    i = 0
    number = 0
    i_list = []
    while i != n:
        if is_simple(number):
            i_list.append(number)
            i += 1
        number += 1

    print(i_list)

def Resheto(n):
    # n = int(input( "вывод простых чисел до числа ... " ))
    n = 30
    a = [ 0 ] * n
    for i in range(n): 
        a[i] = i 

    a[ 1 ] = 0
    m = 2
    while m < n:
        if a[m] != 0 :
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m 
        m += 1

    b = []
    for i in a:
        if a[i] != 0 :
            b.append(a[i])
    del a
    print(b)

cProfile.run('my_func(10)')
cProfile.run('Resheto(30)')

"""
В итоге мой алгоритм выполнился за 0.002 секунды, а алгоритм Решето Эратосфена выпонлися за 0.001 секунду.
Можно сделать вывод, что использовать Решето Эратосфена будет эффективнее.
"""
