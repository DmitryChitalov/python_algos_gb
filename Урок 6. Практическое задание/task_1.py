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
########################################################################################################################

from collections import defaultdict
import time
import memory_profiler

start_t_1 = time.perf_counter()
start_m_1 = memory_profiler.memory_usage()


info = defaultdict(int)


def information(n):
    if n == 0:
        return
    firm_name = input('Введите название предприятия: ')
    profit = sum([int(i) for i in input('Введите прибыль данного предприятия за каждый квартал: ').split()]) / 4
    info[firm_name] = profit
    return information(n - 1)


firms = int(input('Введите количество предприятий для расчета прибыли: '))
information(firms)
average_profit = (sum(info.values()) / firms)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
high = [a[0] for a in info.items() if a[1] > average_profit]
print(f"Предприятия, с прибылью выше среднего значения: {', '.join(high)}")
low = [b[0] for b in info.items() if b[1] < average_profit]
print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(low)}")


stop_t_1 = time.perf_counter()
stop_m_1 = memory_profiler.memory_usage()
print(f'Выполнение заняло {stop_t_1 - start_t_1} сек. и {stop_m_1[0] - start_m_1[0]} Мб')

########################################################################################################################

start_t_2 = time.perf_counter()
start_m_2 = memory_profiler.memory_usage()


info = {}
firms = int(input('Введите количество предприятий для расчета прибыли: '))
itr = firms
while itr > 0:
    firm_name = input('Введите название предприятия: ')
    profit = sum([int(i) for i in input('Введите прибыль данного предприятия за каждый квартал: ').split()]) / 4
    info[firm_name] = profit
    itr -= 1

average_profit = (sum(info.values()) / firms)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
high = [a[0] for a in info.items() if a[1] > average_profit]
print(f"Предприятия, с прибылью выше среднего значения: {', '.join(high)}")
low = [b[0] for b in info.items() if b[1] < average_profit]
print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(low)}")


stop_t_2 = time.perf_counter()
stop_m_2 = memory_profiler.memory_usage()
print(f'Выполнение заняло {stop_t_2 - start_t_2} сек. и {stop_m_2[0] - start_m_2[0]} Мб')

"""
    Код, написанный с использованием рекурсии:
    время: 6.3946
    память: 0.0625
    
    Код с использованием цикла:
    время: 4.8765
    память: 0.0
    
    Вывод: 
        Не стоит пихать рекурсию куда попало, хотя она мне и очень полюбилась.
    Насколько я понял, рекурсию нужно прописывать в том случае, 
    когда идут рекурсивные вычисления, и записывать ее в купе с мемоизацией, в противном же случае, как этот,
    разумнее и практичнее будет писать программу с помощью цикла. 

"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t1 = time.perf_counter()
m1 = memory_profiler.memory_usage()


def one(lst):
    some_list = []
    for i in lst:
        if i % 2 == 0:
            some_list.append(i * i)
    return some_list


t2 = time.perf_counter()
m2 = memory_profiler.memory_usage()
print(f'Время: {t2 - t1}, память: {m2[0] - m1[0]}')


t3 = time.perf_counter()
m3 = memory_profiler.memory_usage()


def two(lst):
    for i in lst:
        if i % 2 == 0:
            yield i * i


a_sub = two([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

t4 = time.perf_counter()
m4 = memory_profiler.memory_usage()
print(f'Время: {t4 - t3}, память: {m4[0] - m3[0]}')


t5 = time.perf_counter()
m5 = memory_profiler.memory_usage()

b = [i * i for i in a if i % 2 == 0]

t6 = time.perf_counter()
m6 = memory_profiler.memory_usage()
print(f'Время: {t6 - t5}, память: {m6[0] - m5[0]}')


"""
Цикл:               Время - 0.099543 сек.  память - 0.01171 Мб
Генератор:          Время - 0.099552 сек.  память - 0.0 Мб
Ген. выражение :    Время - 0.099951 сек.  память - 0.0 Мб

Вывод:
    В данном случае, примеры показывают почти одинаковое время, однако цикл,
    в отличие от остальных,чьи показатели на нуле, запрашивает больше всего памяти, так как создается новый список.
    
    
Версия python - 3.7   OC - 64 bit
"""