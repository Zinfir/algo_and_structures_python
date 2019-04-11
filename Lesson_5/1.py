"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

"""
Реализация через колекции, collections.namedtuple
"""

import collections

n = int(input('Введите количество предприятий: '))

Companies = []

for company in range(n):
    name = input('Введите имя {}-й компании: '.format(company + 1))
    Company = collections.namedtuple(name, ['q1', 'q2', 'q3', 'q4', 'year_earn'])
    q1 = float(input('Введите прибыль за {} квартал: '.format(1)))
    q2 = float(input('Введите прибыль за {} квартал: '.format(2)))
    q3 = float(input('Введите прибыль за {} квартал: '.format(3)))
    q4 = float(input('Введите прибыль за {} квартал: '.format(4)))
    year_earn = q1 + q2 + q3 + q4
    c = Company(q1=q1, q2=q2, q3=q3, q4=q4, year_earn=year_earn)
    Companies.append(c)

print('Список предприятий:')
for company in Companies:
    print(company)

sum = 0
for company in Companies:
    sum += company.year_earn
avg = sum / n

print('Средня прибыль предприятий: {}'.format(avg))
print('Предприятия с прибылью выше среднего: ')
for company in Companies:
    if company.year_earn > avg:
        print(company)
print('Предприятия с прибылью ниже среднего: ')
for company in Companies:
    if company.year_earn < avg:
        print(company)


"""
Реализация без коллекций
"""

# n = int(input('Введите количество предприятий: '))

# Companies = {}

# for company in range(n):
#     name = input('Введите имя {}-й компании: '.format(company + 1))
#     Companies[name] = []
#     year_earn = 0
#     for q in range(4):
#         q_earn = float(input('Введите прибыль за {} квартал: '.format(q + 1)))
#         Companies[name].append(q_earn)
#         year_earn += q_earn
#     Companies[name].append(year_earn)

# for key, value in Companies.items():
#     print('Предприятие - {}, прибыль по кварталам - {}, годовая прибыль - {}'.format(key, value[0:4], value[4]))


# sum = 0
# for key, value in Companies.items():
#     sum += value[4]
# avg = sum / n

# print('Средня прибыль предприятий: {}'.format(avg))
# print('Предприятия с прибылью выше среднего: ')
# for key, value in Companies.items():
#     if value[4] > avg:
#         print('{} - {}'.format(key, value[4]))
# print('Предприятия с прибылью ниже среднего: ')
# for key, value in Companies.items():
#     if value[4] < avg:
#         print('{} - {}'.format(key, value[4]))
