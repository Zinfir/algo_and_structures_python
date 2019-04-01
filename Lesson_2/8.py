"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


while True:
    try:
        find_count = 0
        find_number = int(input('Введите нужное число: '))
        n = int(input('Введите число n, количество чисел последовательности: '))
        count = 0
        while count < n:
            number = int(input('Введите число последовательности: '))
            count += 1
            if find_number == number:
                find_count += 1
        print('Число {} встречается {} раз'.format(find_number, find_count))
        break
    except ValueError:
        print('Введено некорректное значение')
