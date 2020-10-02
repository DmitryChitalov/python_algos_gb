"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from sys import getrefcount
from collections import namedtuple

# python 3.8 разрядность 64

@profile          # namedtuple - 12.1 MiB от начала до конца
def acc_profit():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    firms = {}
    comm_p = 0
    for i in range(n):
        name = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        dat = namedtuple('manuf', 'name profit')
        manufs = dat(name, profit)
        each_prof = sum([int(item) for item in manufs.profit.split()])
        comm_p = comm_p + each_prof
        firms[name] = each_prof
    aver = comm_p / n
    print(f'Средняя прибыль предприятий: {aver}')
    print(f'Предприятия и их годовая прибыль: {firms}')
    a = [key for key in firms if firms[key] < aver]
    b = [key for key in firms if firms[key] > aver]
    print(f'Предприятия, чья прибыль ниже среднего: {a}')
    print(f'Предприятия, чья прибыль выше среднего: {b}')

acc_profit()

@profile            #  использование итератора - 12.1 MiB
def substrings(a):
    length = len(a)
    return [(a[i:j + 1]) for i in range(length) for j in range(i, length)]

substrings('qdfatyrkoikjnhdfreyilmjopvrelafgdoklll')

@profile            #  заполнение словаря добавило 12.0 MiB, заполнение списка- 0.4 MiB
def fill_obj():     #  удаление ссылки на словарь снизило Mem usage с 55.8 до 31.8 MiB
    d = {}
    l = []
    for i in range(100000):
        k = i
        v = i
        d[k] = v
        l.append(i)
    del d
    return

fill_obj()

@profile
def fill_d():      #  Заполение словаря через генератор с последующим удалением ссылки  - 12.2 MiB оптимальнее, чем заполнение в цикле
    d = {a: a ** 2 for a in range(100000)}
    del d
    return

fill_d()

# Вероятно, функция с итерациями оптимальнее для памяти, чем другие
# Функция с namedtuple  - оценить, сколько памяти съест, если ввсети 100000 значений, не могу))
