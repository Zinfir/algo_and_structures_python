# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

n_list = [randint(0, 100) for _ in range(0, 11, 1)]
set_list = set(n_list)

max_count = 0
current_count = 0
max_count_number = 0


for u_number in set_list:
    for number in n_list:
        if u_number == number:
            current_count += 1
    if current_count > max_count:
        max_count_number = u_number
        max_count = current_count
    current_count = 0

print(n_list)
print('Число {} встречается больше всего раз - {}'.format(max_count_number, max_count))
        