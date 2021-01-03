"""
1.	I Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
II Программа должна определить среднюю прибыль (за год для всех предприятий)
III и вывести наименования предприятий, чья прибыль выше среднего и отдельно
IV вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
a Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
b Для лучшее освоения материала можете даже сделать несколько решений этого задания,
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
# a
from collections import Counter
"""
Для решения создадим класс StatisticsFirms
"""


class StatisticsFirms:
    def __init__(self):
        self.profit_lst = []  # Список годовой прибыли для каждой фирмы
        self.firm_dict = {}  # Словарь {название: прибыль за год}
        self.below_average = []  # Список фирм с прибылью ниже средней
        self.above_average = []  # Список фирм с прибылью выше средней

    def firms_and_profit(self):  # I Введение данных от пользователя
        ex = 'yes'
        while ex == 'yes':
            company = input('Введите название предприятия:\n')
            profit = input('Через пробел введите прибыль данного предприятия'
                           'за кажджый квартал(Всего 4 квартала):\n').split(' ')
            if sum(Counter(profit).values()) != 4:  # проверяем, что у нас 4е элемента
                print('Необходимо ввести 4 числа через пробел, попробуйте еще раз')
                continue
            else:
                try:  # приводим все элементы profit к int
                    profit = list(map(int, profit))
                except ValueError:
                    print('Необходимо ввести 4 числа через пробел, попробуйте еще раз')
                    continue
                self.profit_lst.append(sum(profit))
                self.firm_dict[company] = sum(profit)
                ex = input('Желаете продолжить? Yes/no\n').lower()
        return self.firm_dict and self.profit_lst

    def analysis_firms(self):
        """
        определяем среднюю годовую прибыль и находим фирмы с доходом выше и ниже среднего
        """
        middle_year_profit = sum(self.profit_lst)/sum(Counter(self.profit_lst).values())  # II
        for key, value in self.firm_dict.items():
            if value < middle_year_profit:
                self.below_average.append(key)  # IV
            elif value > middle_year_profit:
                self.above_average.append(key)  # III
        return f'Средняя годовая прибыль по указанным предприятиям: {middle_year_profit}\n' \
               f'Предприятия с прибылью выше среднего: {self.above_average}\n' \
               f'Предприятия с прибылью ниже среднего: {self.below_average}.'


an1 = StatisticsFirms()
an1.firms_and_profit()
print(an1.firm_dict)
print(an1.profit_lst)
print(an1.analysis_firms())

"""
Результат работы программы:

Введите название предприятия:
Рога
Через пробел введите прибыль данного предприятияза кажджый квартал(Всего 4 квартала):
235 345634 55
Необходимо ввести 4 числа через пробел, попробуйте еще раз
Введите название предприятия:
Рога
Через пробел введите прибыль данного предприятияза кажджый квартал(Всего 4 квартала):
один два три четыре
Необходимо ввести 4 числа через пробел, попробуйте еще раз
Введите название предприятия:
Рога
Через пробел введите прибыль данного предприятияза кажджый квартал(Всего 4 квартала):
235 345634 55 235
Желаете продолжить? Yes/no
yes
Введите название предприятия:
Копыта
Через пробел введите прибыль данного предприятияза кажджый квартал(Всего 4 квартала):
345 34 543 34
Желаете продолжить? Yes/no
no
{'Рога': 346159, 'Копыта': 956}
[346159, 956]
Средняя годовая прибыль по указанным предприятиям: 173557.5
Предприятия с прибылью выше среднего: ['Рога']
Предприятия с прибылью ниже среднего: ['Копыта'].
"""