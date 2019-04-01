"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
try:
    a = int(input('Введите число: '))
except ValueError:
    print('Введено некорректное значение')

input_a = a
odd_numbers = ''
even_numbers = ''
odd_count = 0
even_count = 0

while a:
    digit = a % 10
    a = a // 10
    if digit % 2:
        odd_numbers += str(digit)
        odd_count += 1
    else:
        even_numbers += str(digit)
        even_count += 1

out_str = 'В числе {0} {1} нечетных ({2}) и {3} четных ({4}) цифр'.format(
        input_a,
        odd_count,
        odd_numbers,
        even_count,
        even_numbers
    )

print(out_str)