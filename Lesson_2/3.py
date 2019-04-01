"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

def recursion(a):
    if (a // 10) == 0:
        return str(a)
    elif (a // 10):
        return str(a % 10) + str(recursion(a // 10))
        
try:
    a = int(input('Введите число: '))
except ValueError:
    print('Введено некорректное значение')
print(recursion(a))
    