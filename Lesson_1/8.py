# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 400 == 0:
            print('Високосный год')
    elif year % 100 == 0:
            print('Не високосный год')
    else:
        print('Високосный год')
else:
    print('Не високосный год')