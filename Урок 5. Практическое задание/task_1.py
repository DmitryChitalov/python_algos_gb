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
from collections import defaultdict, namedtuple


"""
Решение с применением Defaultdict
"""


class AvgProfit:
    def __init__(self):
        self.number_company = int(input('Введите кол-во предприятий для расчета прибыли: '))
        self.company_dict = defaultdict(int)
        self.avg_all_profit = 0
        self.less = []
        self.more = []
        self.data_company()

    def __str__(self):
        return f'Средняя годовая прибыль всех компаний: {str(self.avg_all_profit)}\n' \
               f'Компании с прибылью выше среднего: {str(", ".join(self.more))}\n' \
               f'Компании с прибылью ниже среднего: {str(", ".join(self.less))}'

    def data_company(self):
        for i in range(self.number_company):
            name = input('Название компании: ')
            aver_profit = sum(map(int,
                                  input('Через пробел введите прибыль данного предприятия '
                                        'за каждый квартал (Всего 4 квартала): ').split(' ')))
            self.company_dict[name] = int(aver_profit/4)
        return

    def avg_comp(self):
        self.avg_all_profit = sum([v for v in self.company_dict.values()]) / len(self.company_dict)
        for k, v in self.company_dict.items():
            if v >= self.avg_all_profit:
                self.more.append(k)
            else:
                self.less.append(k)
        return


calculate = AvgProfit()
calculate.avg_comp()
print(calculate)


"""
Решение с применением Namedtuple
"""
num_company = int(input('Введите кол-во компаний: '))
direct_company = {}

# формируем справочник компаний, на выходе словарь со среднеей прибилью каждой компании
for i in range(num_company):
    COMP = namedtuple('Direct', 'name one two three four')
    name_company = input('Введите назнвание компании: ')
    profit_list = input('Через пробел введите прибыль данного компании '
                        'за каждый квартал (Всего 4 квартала): ').split(' ')

    item_company = COMP(
        name=name_company,
        one=int(profit_list[0]),
        two=int(profit_list[1]),
        three=int(profit_list[2]),
        four=int(profit_list[3])
    )
    direct_company[name_company] = (item_company.one + item_company.two + item_company.three + item_company.four) / 4


# Считаем среднюю прибыль всех компаний
aver_profit = 0
for v in direct_company.values():
    aver_profit += v
aver_profit = aver_profit / 4


# определяем компании с доходом выше среднего и ниже среднего
more_profit = []
less_profit = []

for k, v in direct_company.items():
    if v >= aver_profit:
        more_profit.append(k)
    else:
        less_profit.append(k)

print(f'Компании, с прибылью ВЫШЕ среднего значения: {", ".join(more_profit)}\n'
      f'Компании, с прибылью НИЖЕ среднего значения: {", ".join(less_profit)}',)