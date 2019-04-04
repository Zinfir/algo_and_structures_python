# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

n_list = []

for _ in range(2, 10, 1):
    n_list.append([])

for i, number in enumerate(range(2, 100, 1)):
    for j, digit in enumerate(range(2, 10, 1)):
        if number % digit == 0:
            n_list[j].append(number)

for index, item in enumerate(n_list):
    print('Для {}: {} кратных чисел'.format(index + 2, len(item)))
