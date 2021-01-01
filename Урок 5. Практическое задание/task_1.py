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
from collections import deque,OrderedDict
from functools import reduce

def number_input():
    __temp_number = input('Введите количество предприятий для расчета прибыли:')
    try:
        return int(__temp_number)
    except:
        print('Вы ввели не число')
        return number_input()

def quarta_profit_input():
    __temp_quarta_profit = input('''через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала):''')
    try:
        __profits_array = __temp_quarta_profit.split(' ')
        if len(__profits_array) != 4:
            raise ValueError('Вы ввели не 4 числа')
        return deque(int(num) for num in __profits_array)
    except ValueError as e:
        print(e)
        return quarta_profit_input()
    except:
        print('другая непонятная ошибка')
        return quarta_profit_input()

class FirmDatabase:
    def __init__(self,db_size):
        self.size = db_size
        self.db = OrderedDict()
        self.average_profit = 0
        for i in range(self.size):
            self.add_firm(input('Введите название предприятия: '),quarta_profit_input())
        self.calc_average_profit()

    def add_firm(self,name,profit):
        self.db.setdefault(name,dict(profits = profit, summary = reduce(lambda x,y:x+y, profit)))

    def calc_average_profit(self):
        __summary = 0
        for val in self.db.values():
            __summary += val['summary']
        self.average_profit = __summary/self.size

    def divide_by_median(self):
        __lower = deque()
        __upper = deque()
        for key,val in self.db.items():
            if self.average_profit > val['summary']:
                __lower.append(key)
            else:
                __upper.append(key)
        return [__lower,__upper]

    def __str__(self):
        __str = ''
        __str += f'Средняя годовая прибыль всех предприятий: {self.average_profit}\n'
        __lower, __upper = self.divide_by_median()
        __str += f'Предприятия, с прибылью выше среднего значения: {"".join(__upper)}\n'
        __str += f'Предприятия, с прибылью ниже среднего значения: {"".join(__lower)}\n'
        return __str


myFirmDB = FirmDatabase(number_input())
print(myFirmDB)
