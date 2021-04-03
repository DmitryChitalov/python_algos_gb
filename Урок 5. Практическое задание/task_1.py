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
from operator import itemgetter, attrgetter
from statistics import mean

Corp = namedtuple('Corporation', 'name qr total')

num_corp = int(input('Введите количество предприятий для расчета прибыли: '))

data = []
for _ in range(num_corp):
    corp_name = input('Введите название предприятия: ')
    rev_inp = input(
        'Через пробел введите прибыль'
        + 'данного предприятия за каждый квартал\n'
        + '(Всего 4 квартала): ')

    qr = [float(f) for f in rev_inp.split(' ')]
    data.append(Corp(corp_name, qr, sum(qr)))

aver = mean(c.total for c in data)

data.sort(key=attrgetter('total'))
print(f'Средняя годовая прибыль всех предприятий: {aver:.2f}')
print(
    'Предприятия, с прибылью выше среднего значения:',
    ' '.join(c.name for c in data if c.total >= aver))
print(
    'Предприятия, с прибылью ниже среднего значения:',
    ' '.join(c.name for c in data if c.total < aver))

# ---
# Введите количество предприятий для расчета прибыли: 2
# Введите название предприятия: Рога
# Через пробел введите прибыль данного предприятия за каждый квартал
# (Всего 4 квартала): 235 345634 55 235
# Введите название предприятия: Копыта
# Через пробел введите прибыль данного предприятия за каждый квартал
# (Всего 4 квартала): 345 34 543 34
# Средняя годовая прибыль всех предприятий: 173557.50
# Предприятия, с прибылью выше среднего значения: Рога
# Предприятия, с прибылью ниже среднего значения: Копыта
# ---

# вариант, когда данные лежат в csv-файле
csvtext = """\
Company,Q1,Q2,Q3,Q4
SAUDI ARABIAN OIL COMPANY,62.47,25.37,44.2,51.75
APPLE,11.25,11.25,12.67,28.75
MICROSOFT CORPORATION,10.75,11.2,13.89,15.46
ALPHABET,6.84,6.96,11.24,15.23
AMAZON.COM,2.54,5.24,6.33,13.18
FACEBOOK,4.9,5.18,7.84,11.22
ALIBABA GROUP HOLDING,3.16,46.43,26.52,79.43
BERKSHIRE HATHAWAY,29.16,-49.75,26.29,30.41
TENCENT,20.38,21.58,28.89,30.15
J P MORGAN CHASE & CO,2.85,4.68,9.44,12.1"""

data = sorted(
    (
        (n, sum(map(float, d)))
        for n, *d in (
            row.split(',')
            for i, row in enumerate(csvtext.split('\n'))
            if i > 0)),
    key=itemgetter(1), reverse=True)
aver = mean(map(itemgetter(1), data))

print(f'Среднее значение годовой прибыли: {aver:.2f} млрд. USD')
print()
print('Компании, заработавшие больше среднего:')
print('\n'.join(f'{n}: {v:.2f}' for n, v in data if v >= aver))
print()
print('Компании, заработавшие меньше среднего:')
print('\n'.join(f'{n}: {v:.2f}' for n, v in data if v < aver))
print()
# ---
# Среднее значение годовой прибыли: 71.74 млрд. USD
#
# Компании, заработавшие больше среднего:
# SAUDI ARABIAN OIL COMPANY: 183.79
# ALIBABA GROUP HOLDING: 155.54
# TENCENT: 101.00
#
# Компании, заработавшие меньше среднего:
# APPLE: 63.92
# MICROSOFT CORPORATION: 51.30
# ALPHABET: 40.27
# BERKSHIRE HATHAWAY: 36.11
# FACEBOOK: 29.14
# J P MORGAN CHASE & CO: 29.07
# AMAZON.COM: 27.29
# ---

# Это решение задачи на pandas
import pandas
from io import StringIO
qr = pandas.read_csv(StringIO(csvtext))
qr['Y2020'] = qr[['Q1', 'Q2', 'Q3', 'Q4']].sum(axis=1)
qr.sort_values('Y2020', ascending=False, inplace=True)
aver = qr['Y2020'].mean()

print(f'Среднее значение годовой прибыли: {aver:.2f} млрд. USD')
print()
print('Компании, заработавшие больше среднего:')
print(qr[qr.Y2020 >= aver][['Company', 'Y2020']].to_string(index=False))
print()
print('Компании, заработавшие меньше среднего:')
print(qr[qr.Y2020 < aver][['Company', 'Y2020']].to_string(index=False))
print()
# ---
# Среднее значение годовой прибыли: 71.74 млрд. USD
#
# Компании, заработавшие больше среднего:
#                   Company  Y2020
# SAUDI ARABIAN OIL COMPANY 183.79
#     ALIBABA GROUP HOLDING 155.54
#                   TENCENT 101.00
#
# Компании, заработавшие меньше среднего:
#               Company  Y2020
#                 APPLE  63.92
# MICROSOFT CORPORATION  51.30
#              ALPHABET  40.27
#    BERKSHIRE HATHAWAY  36.11
#              FACEBOOK  29.14
# J P MORGAN CHASE & CO  29.07
#            AMAZON.COM  27.29
# ---
