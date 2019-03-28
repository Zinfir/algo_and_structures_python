"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random
range = input("Введите начало и конец диапозона через пробел: ")
start, end = str(range).split(" ")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = []
for letter in alphabet:
    alphabet_list.append(letter)

try:
    start = float(start)
    end = float(end)
    if start % 1 != 0 and end % 1 != 0:
        print('Случайное вещественное число: ', start + random()*(end - start))
    elif start % 1 == 0 and end % 1 == 0:
        print('Случайное целое число: ', int(start + random()*(end - start)))  
except:
    if start in alphabet and end in alphabet:
        for index, letter in enumerate(alphabet_list):
            if letter == start:
                start_index = index
            elif letter == end:
                end_index = index
        
        rand_index = int(start_index + random()*(end_index - start_index))
        print('Случайный символ: ', alphabet_list[rand_index])
