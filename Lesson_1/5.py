#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

range = input("Введите две буквы через пробел: ")
start, end = str(range).split(" ")

if end < start:
    start, end = end, start


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = []
for letter in alphabet:
    alphabet_list.append(letter)


if start in alphabet and end in alphabet:
    for index, letter in enumerate(alphabet_list):
        if letter == start:
            start_index = index + 1
        elif letter == end:
            end_index = index + 1
    print("Местонахождение: {} {}, Расстояние: {}".format(start_index, end_index, (end_index - start_index + 1)))
