# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = int(input('Введите номер буквы: '))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = []
for letter in alphabet:
    alphabet_list.append(letter)

if 1 < number < 26:
    print('Буква: ', alphabet_list[number - 1])
