# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
while True:
    try:
        number = input("Введите число: ")
        tmp_number = abs(int(number))
        break
    except ValueError:
        print("ValueError: Введено некорректное значение числа, повторите ввод.")

tmp_list = []

while tmp_number != 0:
    digit = tmp_number % 10
    tmp_list.append(digit)
    tmp_number = int(tmp_number * 0.1)

sum = 0
multiplication = 0

for index, digit in enumerate(tmp_list):
    sum += digit
    if index == 0:
        multiplication = digit
    else:
        multiplication *= digit

print("Сумма цифр числа {0} равна: {1}\nПроизведение цифр числа {0} равно: {2}".format(
    number, sum, multiplication
    ))
