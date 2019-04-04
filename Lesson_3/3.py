#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

n_list = [randint(0, 100) for _ in range(0, 11, 1)]
print(n_list)

n_max = max(n_list)
n_min = min(n_list)
max_index = n_list.index(n_max)
min_index = n_list.index(n_min)
n_list.insert(max_index, n_list.pop(min_index))
if max_index < min_index:

    n_list.insert(min_index, n_list.pop(max_index + 1))
else:
    n_list.insert(min_index, n_list.pop(max_index - 1))

print(n_list)
