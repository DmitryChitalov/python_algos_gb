"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""


import collections
from numpy import sum


def rec_sum_el_array(array, result=0):
    if not result:
        result = []
    if len(array) == 0:
        pass
    else:
        result.append(int(sum(list(array.popleft()[1:5]))))  # метод для deque
        rec_sum_el_array(array, result)
        return result


while True:
    try:
        company_count = int(input('Введите количество предприятий для расчета прибыли: '))
        break
    except ValueError:
        print('Введено некорректное значение')

my_bd = []
year_profit = []
for i in range(company_count):
    companies = collections.namedtuple('Companies', 'Name I II III IV')
    name = input('Введите название предприятия: ')

    while True:
        try:
            profit = list(map(int, input('через пробел введите прибыль данного предприятия \n'
                                         'за каждый квартал(Всего 4 квартала): ').split()))
            my_namedtuple = companies(
                Name=name,
                I=int(profit[0]),
                II=int(profit[1]),
                III=int(profit[2]),
                IV=int(profit[3])
            )
            break
        except ValueError:
            print('Введено некорректное значение')
        except IndexError:
            print('Введено недостаточное количество данных')

    print('')
    my_bd.append(my_namedtuple)
    year_profit.append(sum(my_namedtuple[1:len(my_namedtuple)+1]))  # простое решение

# решение через рекурсию c применением deque
# my_deq_bd = collections.deque(my_bd)
# year_profit = rec_sum_el_array(my_deq_bd)

general_average = sum(year_profit) / len(year_profit)

more_gen_ave = ''
less_gen_ave = ''
print(f'Средняя годовая прибыль всех предприятий: {general_average}')
for i in range(len(year_profit)):
    if year_profit[i] > general_average:
        more_gen_ave += f'{my_bd[i].Name} '
    else:
        less_gen_ave += f'{my_bd[i].Name} '
print(f'Предприятия, с прибылью выше среднего значения: {more_gen_ave if more_gen_ave != "" else "Нет"}\n')
print(f'Предприятия, с прибылью ниже среднего значения: {less_gen_ave if less_gen_ave != "" else "Нет"}')
