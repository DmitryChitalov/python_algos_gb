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
from random import randint


#  example 1


@profile
def calc_salary(*args):
    """ This program counts salary """

    try:
        # prod_in_hours, rate_per_hour, bonus = check_and_parsing_argv(*args)
        result = int(prod_in_hours) * int(rate_per_hour)
        if bonus:
            result += result * int(bonus) / 100
            return result
        else:
            return result
    except TypeError:
        return 'Необходимо ввести цифры через пробел: выработка в часах, ставка в час, размер премии (в %)'
    except ValueError:
        return 'Необходимо вводить целые числа!'


prod_in_hours, rate_per_hour, bonus = 160, 500, 25

salary = calc_salary(prod_in_hours, rate_per_hour, bonus)

if type(salary) == float or type(salary) == int:
    print(f'Заработная плата за месяц равна: {salary} (до вычета налогов)')
else:  # Возвращаем ошибку из except
    print(salary)

"""
Line #    Mem usage    Increment   Line Contents
================================================
    20     13.2 MiB     13.2 MiB   @profile
    21                             def calc_salary(*args):
    22                                 ''' This program counts salary '''
    23                             
    24     13.2 MiB      0.0 MiB       try:
    25                                     # prod_in_hours, rate_per_hour, bonus = check_and_parsing_argv(*args)
    26     13.2 MiB      0.0 MiB           result = int(prod_in_hours) * int(rate_per_hour)
    27     13.2 MiB      0.0 MiB           if bonus:
    28     13.2 MiB      0.0 MiB               result += result * int(bonus) / 100
    29     13.2 MiB      0.0 MiB               return result
    30                                     else:
    31                                         return result
    32                                 except TypeError:
    33                                     return 'Необходимо ввести цифры через пробел: выработка в часах, ставка в 
                                           час, размер премии (в %)'
    34                                 except ValueError:
    35                                     return 'Необходимо вводить целые числа!'
    
Вывод: в данной программе нечего оптимизировать, ветвления и конструкции try/except не расходуют лишнюю память
"""


# example 2


@profile
def bad_search(_list):
    _var = 0
    while True:
        if _var not in _list:
            _var += 1
        else:
            return _var


@profile
def good_search(_list):
    return min(_list)


work_list = [randint(1, 200) for x in range(1, 200)]

print(f'Наименьшее значение в рандомном списке: {bad_search(work_list)}')
print(f'Наименьшее значение в рандомном списке: {good_search(work_list)}')

"""
Line #    Mem usage    Increment   Line Contents
================================================
    75     13.1 MiB     13.1 MiB   @profile
    76                             def bad_search(_list):
    77     13.1 MiB      0.0 MiB       _var = 0
    78                                 while True:
    79     13.1 MiB      0.0 MiB           if _var not in _list:
    80     13.1 MiB      0.0 MiB               _var += 1
    81                                     else:
    82     13.1 MiB      0.0 MiB               return _var


Наименьшее значение в рандомном списке: 1
Filename: C:/Users/NPC/PycharmProjects/pythonProject/lesson_6/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    85     13.1 MiB     13.1 MiB   @profile
    86                             def good_search(_list):
    87     13.1 MiB      0.0 MiB       return min(_list)


Наименьшее значение в рандомном списке: 1

Вывод: 
Код также не требует оптимизации. Мы видим, что два алгоритма поиска, которые занимают разное количество времени, 
при всём при этом не имеют проблем с памятью. Из этого следует, что прямой связи между временными затратами на исполне-
ние кода и количеством выделяемой памяти нет. 

P.S.: Я просмотрел все ДЗ по "Основам" и не нашёл кода, требующего оптимизации по памяти, поэтому здесь только 2 примера
"""
