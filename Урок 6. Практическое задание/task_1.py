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
from random import randint, random
from timememit import timememit
from pympler.asizeof import asizeof
from recordclass import recordclass
from datetime import datetime, timedelta
import numpy as np
import json
import msgpack
import sys


args = iter(sys.argv)
next(args)
ARG1 = next(args, None)
NOW = datetime.now()
LETRANGE = (ord('A'), ord('Z'))

# Будем применять способы оптимизации памяти, рассмотренные на уроке

# 1. Ленивые вычисления
# пример в файле task_3a.py

# 2. Слоты в ООП
# 3. numpy (также пример в файле task_2.py)
# 4. recordclass


# Пусть у нас есть список чего-либо, допустим, биржевой торговли
def gen_transaction():
    return (
        # ticker
        ''.join(chr(randint(*LETRANGE)) for _ in range(4)),
        # number
        randint(1, 1000),
        # seller_id
        randint(1, 10000000),
        # buyer_id
        randint(1, 10000000),
        # price
        randint(1, 10000000),
        # timestamp
        NOW + timedelta(seconds=randint(0, 100000))
    )


class Transaction:
    def __init__(self, ticker, number, seller, buyer, price, timestamp):
        self.ticker = ticker
        self.number = number
        self.seller = seller
        self.byer = buyer
        self.price = price
        self.timestamp = timestamp


class TransSlots:
    __slots__ = ['ticker', 'number', 'seller', 'buyer', 'price', 'timestamp']

    def __init__(self, ticker, number, seller, buyer, price, timestamp):
        self.ticker = ticker
        self.number = number
        self.seller = seller
        self.buyer = buyer
        self.price = price
        self.timestamp = timestamp


TransRecord = recordclass(
    'TransRecord',
    'ticker number seller buyer price timestamp')

trans_dtype = [
        ('ticks', '<U4'),
        ('number', '<i4'),
        ('seller', '<i4'),
        ('buyer', '<i4'),
        ('price', '<i4'),
        ('timestamp', 'datetime64[m]')]

if ARG1 is None:
    n = 1000
    classes = [Transaction(*gen_transaction()) for i in range(n)]
    slots = [TransSlots(*gen_transaction()) for i in range(n)]
    records = [TransRecord(*gen_transaction()) for i in range(n)]
    nprecords = np.array(
        [gen_transaction() for i in range(n)],
        dtype=trans_dtype)

    print(f'Размер массива из {n} элементов')
    print(f'      class: {asizeof(classes)}')
    print(f'  __slots__: {asizeof(slots)}')
    print(f'recordclass: {asizeof(records)}')
    print(f'      numpy: {asizeof(nprecords)}')
# ---
# Размер массива из 1000 элементов
#       class: 429648
#   __slots__: 318232
# recordclass: 82176
#       numpy: 40120
# ---
# Практически невозможно "победить" по потреблению памяти numpy,
# но у этого есть своя цена, массивы numpy фиксированного размера,
# поэтому их применение подходит не для всех алгоритмов.
# recordclass по результатам измерений на втором месте, но это
# дополнительный модуль, компилируемый в бинарный код, что
# накладывает некоторые ограничения на развертывание приложения.
# __slots__ является частью языка и этих ограничений не имеет,
# однако в данном примере не видно большого уменьшения памяти.

# 5. map
# map можно отнести к ленивым вычислениям,
# в python3 map(f, seq) без потерь по производительности
# и памяти можно заменять на (f(x) for x in seq)

# 6. Сериализация
# Продположим у нас есть сервер, к которому подключаются
# пользоатели, для каждого из которых нужно хранить
# много данных.
# Можно разделить пользователей по частоте обращения,
# и данные "заснувших" сессий сериализовать.


# Для примера построим дерево cо строчками на крайних ветках
def gen_tree(deep=5):
    if deep == 0:
        return str(randint(1, 99))
    newdeep = deep - 1
    return [gen_tree(newdeep), gen_tree(newdeep)]


if ARG1 == "6":
    tree = gen_tree(20)
    print(
        f'                Размер объекта в памяти: {asizeof(tree)}')
    print(
        f'   Размер сериализованных данных (json): {len(json.dumps(tree))}')
    print(
        f'Размер сериализованных данных (msgpack): '
        + f'{len(msgpack.packb(tree, use_bin_type=True))}')
# ---
#                 Размер объекта в памяти: 134217656
#    Размер сериализованных данных (json): 8293148
# Размер сериализованных данных (msgpack): 4098847
# ---
