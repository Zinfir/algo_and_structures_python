"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

defdict = collections.defaultdict(list)

a = 'A2'
A = [_ for _ in a]

b = 'C4F'
B = [_ for _ in b]

def_dict = collections.defaultdict(list)

def_dict[a] = A
def_dict[b] = B

print(def_dict)
value_A = 0
for index, value in enumerate(def_dict[a][::-1]):
    value_A += int(value, 16) * 16**index

value_B = 0
for index, value in enumerate(def_dict[b][::-1]):
    value_B += int(value, 16) * 16**index

sum = value_A + value_B
mul = value_A * value_B

sum_hex = hex(sum)[2:]
mul_hex = hex(mul)[2:]
SUM = [_ for _ in sum_hex]
MUL = [_ for _ in mul_hex]
def_dict[sum_hex] = SUM
def_dict[mul_hex] = MUL

for index, item in enumerate(def_dict):
    if index == 0:
        print('Первое число: ', item)
    elif index == 1:
        print('Второе число: ', item)
    elif index == 2:
        print('Сумма:        ', item)
    elif index == 3:
        print('Умножение:    ', item)
