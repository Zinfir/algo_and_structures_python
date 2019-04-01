"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sum(a):
    sum = 0
    while a:
        digit = a % 10
        a = a // 10
        sum += digit
    return sum


while True:
    try:
        n = int(input('Введите число n, количество натуральных чисел: '))
        count = 0
        max_sum = 0
        cur_sum = 0
        max_number = 0
        while count < n:
            number = int(input('Введите натуральное число: '))
            count += 1
            cur_sum = sum(number)
            if max_sum < cur_sum:
                max_sum = cur_sum
                max_number = number
            
        print('Число с максимальной суммой цифр - {}, сумма цифр = {}'.format(max_number, max_sum))
        break
    except ValueError:
        print('Введено некорректное значение')