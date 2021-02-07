"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from random import randint
from memory_profiler import profile, memory_usage
import json
from pympler import asizeof


def decorator(f):
    def wrapper(*args):
        m1 = memory_usage()
        res = f(args)
        m2 = memory_usage()
        delta_m = m2[0] - m1[0]
        return res, delta_m

    return wrapper


# скрипт № 1 который я взял заполнение списка
@profile
def fill_list(n):
    nums_list = [randint(0, 20) for i in range(n)]
    return nums_list


@decorator
def fill_list_1(n):
    i = 0
    while i < n[0]:
        i += 1
        yield randint(0, 20)


my_gen, sum_m = fill_list_1(100000)
for i in my_gen:
    print(i)
print(f'мое новое значение памяти {sum_m}')

fill_list(100000)
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     13.5 MiB     13.5 MiB           1   @profile
    41                                         def fill_list(n):
    42     14.3 MiB      0.8 MiB      100003       nums_list = [randint(0, 20) for i in range(n)]
    43     14.3 MiB      0.0 MiB           1       return nums_list
    
Я взял за основу скрипт из прошлых занятий по заполнению списка. На большом количестве элементов на функцию тратиться 
почти 1 mib памяти. В качестве улучшения я сделал итератор, тогда память стала занимать 0.00390625 так как ячейка памяти
занята только одна и в памяти весь список не храниться. А результат я получил почти такой же тот же список
только получаю я его поэлементно. Если мне сразу не нужен весь список то такой вариант вполне может сойти
за оптимизацию памяти.
'''


# скрипт № 2 который я взял заполнение словаря
@profile
def fill_dict(n):
    nums_dic = {i: randint(0, 20) for i in range(n)}
    return nums_dic


@profile
def fill_dict_new(n):
    nums_dic = {i: randint(0, 20) for i in range(n)}
    nums_dic = json.dumps(nums_dic)
    return nums_dic


fill_dict(100000)
fill_dict_new(100000)

'''
Второй скрипт я так же взял из прошлого урока где сравнивал время заполнения списка и заполнения словаря
К слову сказать функция заполнение словаря значительно больше потребляет памяти чем заполнение списка
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    79     14.6 MiB     14.6 MiB           1   @profile
    80                                         def fill_dict(n):
    81     26.2 MiB     11.6 MiB      100003       nums_dic = {i: randint(0, 20) for i in range(n)}
    82     26.2 MiB      0.0 MiB           1       return nums_dic

В качестве оптимизации я преобразовал выдаваемый список в json и тогда потребление памяти даже уменьшилось
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    84     25.8 MiB     25.8 MiB           1   @profile
    85                                         def fill_dict_new(n):
    86     25.8 MiB  -6729.1 MiB      100003       nums_dic = {i: randint(0, 20) for i in range(n)}
    87     24.6 MiB     -1.2 MiB           1       nums_dic = json.dumps(nums_dic)
    88     24.6 MiB      0.0 MiB           1       return nums_dic

хотя цифра -6729 мне не совсем понятна. Но итоговое значение на 87 строке стало -1.2 MiB

'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        _income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: : {int(self.wage) + int(self.bonus)}')


class Worker_new:
    __slots__ = 'name', 'surname', 'position', 'wage', 'bonus'


class Position_new(Worker_new):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: : {int(self.wage) + int(self.bonus)}')


worker_1 = Position('Vasya', 'Ivanov', 'accounter', 25000, 10000)
worker_2 = Position_new()
worker_2.name = 'Vasya'
worker_2.surname = 'Ivanov'
worker_2.position = 'accounter'
worker_2.wage = 25000
worker_2.bonus = 10000

print(f'Мой начальный вариант: {asizeof.asizeof((worker_1))}')
print(f'Мой доработаный вариант: {asizeof.asizeof((worker_2))}')

'''
Пример взял из вводного курса по python. Померил сколько изначально занимает экземпляр класса. Потом поработал над ним 
путем применения слотов. Результат даже на таком малом объеме получился экономия почти 30 %
Мой начальный вариант: 680
Мой доработаный вариант: 432

В целом по результатам работы можно сделать такой вывод что словари в python это более медленный и более тяжелый
тип данных чем список. И если есть возможность то лучше словарь заменять списком. А если нужно использовать
словарь и он очень тяжелый то можно его заворачивать в json. 
'''

