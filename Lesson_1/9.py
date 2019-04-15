# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

min = min(a, b, c)
max = max(a, b, c)
if min < a < max:
    print('Среднее: ', a)
elif min < b < max:
    print('Среднее: ', b)
elif min < c < max:
    print('Среднее: ', c)