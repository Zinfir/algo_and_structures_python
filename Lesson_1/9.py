# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

min = min(a, b, c)
max = max(a, b, c)
if min < a < max:
    print('Среднее: ', a)
elif min < b < max:
    print('Среднее: ', b)
elif min < c < max:
    print('Среднее: ', c)