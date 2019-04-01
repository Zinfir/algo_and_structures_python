"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

index = 32
end = 127

while index <= end:
    count = 0
    while count < 10 and index <= end:
        if index > 99:
            print('|  {} {} |'.format(index, chr(index)), end='')
        else:
            print('|  {} {}  |'.format(index, chr(index)), end='')
        count += 1
        index += 1
    print('')