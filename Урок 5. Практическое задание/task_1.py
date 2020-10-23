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

# Первая реализация через Counter
import collections

counter = collections.Counter()

n = int(input("Введите количество предприятий для расчета прибыли: "))
for i in range(n):
    cname = input("Введите название предприятия: ")
    point = list(
        map(int, input("Через пробел введите прибыль данного предприятия за каждый квартал(всего 4):  ").split()))
    for s in point:
        counter[cname] += s

avg_common = sum(counter.values()) / n

lst1 = [k for k, v in counter.items() if v > avg_common]
lst2 = [k for k, v in counter.items() if v < avg_common]

print(f'Предприятия, с прибылью выше среднего значения: {", ".join(lst1)}',
      f'Предприятия, с прибылью ниже среднего значения: {", ".join(lst2)}')

# вторая реализация через defaultdict

defdict = collections.defaultdict(int)

n = int(input("Введите количество предприятий для расчета прибыли: "))
for i in range(n):
    cname = input("Введите название предприятия: ")
    point = list(
        map(int, input("Через пробел введите прибыль данного предприятия за каждый квартал(всего 4):  ").split()))
    for s in point:
        defdict[cname] += s

avg_common = sum(defdict.values()) / n

lst1 = [k for k, v in defdict.items() if v > avg_common]
lst2 = [k for k, v in defdict.items() if v < avg_common]

print(f'Предприятия, с прибылью выше среднего значения: {", ".join(lst1)}',
      f'Предприятия, с прибылью ниже среднего значения: {", ".join(lst2)}')

