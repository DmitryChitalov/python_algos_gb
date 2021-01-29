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

import memory_profiler as mp
from collections import deque, defaultdict

start_point = mp.memory_usage()

company_amount = int(input("Введите кол-во компаний: "))
company_info_deque = deque()
average_deque = deque()

while company_amount:
    company_name = input("Введите название предприятия: ")
    income = input("Через пробел введите прибыль данного предприятия "
                   "за каждый квартал(Всего 4 квартала): ")
    income = list(map(lambda x: int(x), income.split(" ")))
    income.insert(0, company_name)
    company_info_deque.append(income)
    company_amount -= 1

[average_deque.append([x[0], sum(x[1:])]) for x in company_info_deque]

average_income = 0
for x in average_deque:
    average_income += x[1]

average_income = average_income / len(average_deque)

print(f"Средняя годовая прибыль всех предприятий: {average_income}")

print("Предприятия, с прибылью выше среднего значения: ", end='')
for x in average_deque:
    if x[1] > average_income:
        print(x[0], end=' ')

print("\nПредприятия, с прибылью ниже среднего значения: ", end=' ')
for x in average_deque:
    if x[1] < average_income:
        print(x[0], end='')

end_point = mp.memory_usage()

print("\n",end_point[0] - start_point[0])

"""
Зайдействованная память равна  0.08203125 MiB, допонительной оптимизации не требуется
"""

start_point = mp.memory_usage()

first_number = list(input("Введите первое число: "))
second_number = list(input("Введите второе число: "))

first_default_dict = defaultdict(int)
second_default_dict = defaultdict(int)

for el in first_number:
    first_default_dict[el] = el

for el in second_number:
    second_default_dict[el] = el


def get_number(your_dict):
    if len(your_dict) == 1:
        return str(your_dict.popitem()[1])
    return str(your_dict.popitem()[1]) + get_number(your_dict)


x = get_number(first_default_dict)
y = get_number(second_default_dict)

x = x[::-1]
y = y[::-1]

overall_sum = hex(int(x, 16) + int(y, 16))
overall_mul = hex(int(x, 16) * int(y, 16))

print("Сумма равна:", [x.upper() for x in list(overall_sum)[2:]])
print("Произведение равно:", [x.upper() for x in list(overall_mul)[2:]])

end_point = mp.memory_usage()
print(end_point[0] - start_point[0])

"""
Зайдействованная память равна  0.01953125 MiB, допонительной оптимизации не требуется
"""


start_point = mp.memory_usage()


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


number = int(input("Введите число: "))

revers(number)
revers_2(number)
revers_3(number)

end_point = mp.memory_usage()
print(end_point[0] - start_point[0])

"""
Зайдействованная память равна  0,0234375 MiB, допонительной оптимизации не требуется
"""