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
from collections import namedtuple
from functools import reduce
from memory_profiler import profile
from memory_profiler import memory_usage


"""
Задача 1. Создание списка пользователей с 4мя полями.

Предложено 4 решения.
1. Посредством стандартного ООП
2. ООП с использованием __slots__
3. Решение с использованием словаря.
4. Решение с использованием именнованного кортежа

При решении используются профилировщик @profiler и созданный мною декоратор @memory_usage_decorator,
Прирост по @profiler'у может быть незаметен. С другой стороны показатели по memory_usage снимаются до вызова функции и после него.
А следовательно память уже подчищена GC
Приведу выписки только показательные по задаче 1, остальной анализ можно увидеть запустив программу:

1. Стандартное решение посредством ООП
Line #    Mem usage    Increment  Occurences   Line Contents
...
    70     20.1 MiB      0.0 MiB      100001       for i in range(prime_number):
    71     20.1 MiB      0.0 MiB      100000           user = Users(f"User_name_{i}", "some_plan", randint(1994, 2021), randint(100000001, 199999999))
Использовано 0.27734375 Mb памяти.

2. Решение посредствам ООП с использованием __slots__
Line #    Mem usage    Increment  Occurences   Line Contents
...
    97     20.2 MiB      0.0 MiB      100001       for i in range(prime_number):
    98     20.2 MiB      0.0 MiB      100000           user = Users_slots(f"User_name_{i}", "some_plan", randint(1994, 2021), randint(10000001, 19999999))
Использовано 0.01953125 Mb памяти.

3. Создание обыкновенного словаря

Использовано 26.5078125 Mb памяти. (Внутри функции)

Line #    Mem usage    Increment  Occurences   Line Contents
...
   105     20.2 MiB      0.0 MiB           1       users_dict = {}
   106     46.7 MiB     11.0 MiB      100001       for i in range(prime_number):
   107     46.7 MiB     15.5 MiB      100000           users_dict[f"User_name_{i}"] = ["some_plan", randint(1994, 2021), randint(10000001, 19999999)]
Использовано 0.7890625 Mb памяти. - показания сняты до и после вызова функции. Память к этому моменту уже подчистилась GC

4. Создание именованного кортежа
Line #    Mem usage    Increment  Occurences   Line Contents
   116     21.0 MiB      0.0 MiB      100001       for i in range(prime_number):
   117     21.0 MiB      0.0 MiB      100000           Users._make([f"User_name_{i}", "some_plan", randint(1994, 2021), randint(10000001, 19999999)])
Использовано 0.0 Mb памяти.

Итого по задаче 1: 
4. Создание именованного кортежа - минимальный расход памяти
2. Решение посредствам ООП с использованием __slots__ - незначительный расход памяти
1. Стандартное решение посредством ООП - в несколько десятков раз проигрывает решению с исп __slots__
3. Создание обыкновенного словаря - Не выдерживает никакой критики. Крайне пямятизатратное.



"""

def memory_usage_decorator(func_name):
    def wrapper(*args):
        m1 = memory_usage()
        func_name(*args)
        m2 = memory_usage()
        print(f"Использовано {m2[0] - m1[0]} Mb памяти.")
    return wrapper


# решение 1. ООП
class Users:
    login: str
    t_plan: str
    agreement_year: int
    id_number: int

    def __init__(self, login, t_plan, agreement_year, id_number):
        self.login = login
        self.t_plan = t_plan
        self.agreement_year = agreement_year
        self.id_number = id_number

    # def __new__(cls, *args, **kwargs):

    def get_id_number(self, login):
        return self.id_number

    def get_agreement_year(self, login):
        return self.agreement_year

    def get_t_plan(self, login):
        return self.t_plan


@memory_usage_decorator
@profile
def oop_users(prime_number: int):
    for i in range(prime_number):
        user = Users(f"User_name_{i}", "some_plan", randint(1994, 2021), randint(100000001, 199999999))


#  решение 2 с использованием __slots__
class Users_slots:
    __slots__ = 'login', 't_plan', 'agreement_year', 'id_number'

    def __init__(self, login, t_plan, agreement_year, id_number):
        self.login = login
        self.t_plan = t_plan
        self.agreement_year = agreement_year
        self.id_number = id_number

    def get_id_number(self, login):
        return self.id_number

    def get_agreement_year(self, login):
        return self.agreement_year

    def get_t_plan(self, login):
        return self.t_plan


@memory_usage_decorator
@profile
def oop_slots_users(prime_number: int):
    for i in range(prime_number):
        user = Users_slots(f"User_name_{i}", "some_plan", randint(1994, 2021), randint(10000001, 19999999))


#  решение 3 с использованием словаря:
@memory_usage_decorator
@profile
def dict_of_users(prime_number: int):
    m1 = memory_usage()
    users_dict = {}
    for i in range(prime_number):
        users_dict[f"User_name_{i}"] = ["some_plan", randint(1994, 2021), randint(10000001, 19999999)]
    m2 = memory_usage()
    print(f"Использовано {m2[0] - m1[0]} Mb памяти. (Внутри функции)")


#  решение 4 c использованием именнованного кортежа
@memory_usage_decorator
@profile
def namedtuple_of_users(prime_number: int):
    Users = namedtuple('Users', ['login', 't_plan', 'agreement_year', 'id_number'])
    user = []
    for i in range(prime_number):
        Users._make([f"User_name_{i}", "some_plan", randint(1994, 2021), randint(10000001, 19999999)])


# Замеры задача 1. Вызовы. Объединила в отдельную функцию, чтоб удобно было отлаживать.
def oop_func_calls():
    prime_number = 100000
    # 1
    print("1. Стандартное решение посредством ООП")
    oop_users(prime_number)
    # 2
    print("2. Решение посредствам ООП с использованием __slots__")
    oop_slots_users(prime_number)
    # 3
    print("3. Создание обыкновенного словаря")
    dict_of_users(prime_number)
    # 4
    print("4. Создание именованного кортежа")
    namedtuple_of_users(prime_number)

oop_func_calls()
