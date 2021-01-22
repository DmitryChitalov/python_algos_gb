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
from collections import namedtuple

count = 0
firms = []
sum_profit = 0

while True:
    try:
        total_firm = int(input('Введите количество предприятий для расчета прибыли: '))
        break
    except ValueError:
        print('Вы ввели не число. Попробуйте еще раз.')

while count < total_firm:
    count += 1
    name = input('Введите название предприятия: ')
    quarter = input('Через пробел введите прибыль данного предприятия\nза каждый квартал(4 квартала): ').split(' ')
    quarters = []
    for i in quarter:
        if len(quarter) != 4:
            print('Вы ошиблись и ввели не правильные данные прибыли предприятия. Попробуйте заново.')
            raise SystemExit(1)
        try:
            quarters.append(int(i))
        except ValueError:
            print('Вы ошиблись и ввели не правильные данные прибыли предприятия. Попробуйте заново.')
            raise SystemExit(1)
    sum_quarters = sum(quarters)
    result = namedtuple('firm', 'name quarter_1 quarter_2 quarter_3 quarter_4 sum_quarters')
    try:
        firm = result(
            name=name,
            quarter_1=quarters[0],
            quarter_2=quarters[1],
            quarter_3=quarters[2],
            quarter_4=quarters[3],
            sum_quarters=sum_quarters
        )
    except IndexError:
        break
    firms.append(firm)

for i in range(len(firms)):
    print(firms[i])
    sum_profit += firms[i].sum_quarters

try:
    average_profit = sum_profit / len(firms)
    print(f'Средняя годовая прибыль всех предприятий: {round(average_profit, 2)}')
    more_avarage = ''
    less_avarage = ''
    for i in range(len(firms)):
        if firms[i].sum_quarters > average_profit:
            more_avarage += firms[i].name + ' '
        else:
            less_avarage += firms[i].name + ' '
    print(f'Предприятия, с прибылью выше среднего значения: {more_avarage}')
    print(f'Предприятия, с прибылью ниже среднего значения: {less_avarage}')
except ZeroDivisionError:
    print('Вы ошиблись и ввели не правильные данные. Попробуйте заново.')
    
"""
Получилось очень много кода, пытался обработь максимум исключений, которые возникали. 
Как лучше решать такие задачи, так как написал или лучше функциями?
"""
