#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


from random import randint

n_list = [randint(-100, 100) for _ in range(0, 11, 1)]

print(n_list)
abs_min = abs(min(n_list))
find_number = 0
find_number_index = 0

for index, number in enumerate(n_list):
    if number < 0 and abs(number) < abs_min:
        abs_min = abs(number)
        find_number = number
        find_number_index = index

print(find_number)
print(find_number_index)
