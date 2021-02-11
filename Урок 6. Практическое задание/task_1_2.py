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

from pympler import asizeof
from sys import getsizeof


class OrgTechniks:

    def __init__(self, name, color, mass):
        self.name = name
        self.color = color
        self.mass = mass


# класс с использованием слотов
class OrgTechniksSlots:
    __slots__ = ('name', 'color', 'mass')

    def __init__(self, name, color, mass):
        self.name = name
        self.color = color
        self.mass = mass


class Printer(OrgTechniks):

    def __init__(self, typ):
        self.type = typ


class Scanner(OrgTechniks):

    def __init__(self, res):
        self.resolution = res


class Xerox(OrgTechniks):

    def __init__(self, speed):
        self.speed = speed


# Классы с использованием слотов
class PrinterSlots(OrgTechniksSlots):
    __slots__ = ('type')

    def __init__(self, typ):
        self.type = typ


class ScannerSlots(OrgTechniksSlots):
    __slots__ = ('resolution')

    def __init__(self, res):
        self.resolution = res


class XeroxSlots(OrgTechniksSlots):
    __slots__ = ('speed')

    def __init__(self, speed):
        self.speed = speed


class Store:
    store_item: dict

    def __init__(self):
        self.store_item = {}

    def add_to_store(self, item_to_add: OrgTechniks, kol: int):
        try:
            current_kol = self.store_item.pop(item_to_add)
        except KeyError:
            current_kol = 0

        current_kol += kol
        self.store_item.update({item_to_add: current_kol})

    def remove_from_store(self, item_to_remove: OrgTechniks, kol: int):
        try:
            current_kol = self.store_item[item_to_remove]
        except KeyError:
            current_kol = 0

        if current_kol >= kol:
            self.store_item.update({item_to_remove: current_kol - kol})
            return True
        else:
            print("На складе недостаточно оргтехники")


# класс с использованием слотов
class StoreSlots:
    __slots__ = ('store_item')

    def __init__(self):
        self.store_item = {}

    def add_to_store(self, item_to_add: OrgTechniksSlots, kol: int):
        try:
            current_kol = self.store_item.pop(item_to_add)
        except KeyError:
            current_kol = 0

        current_kol += kol
        self.store_item.update({item_to_add: current_kol})

    def remove_from_store(self, item_to_remove: OrgTechniksSlots, kol: int):
        try:
            current_kol = self.store_item[item_to_remove]
        except KeyError:
            current_kol = 0

        if current_kol >= kol:
            self.store_item.update({item_to_remove: current_kol - kol})
            return True
        else:
            print("На складе недостаточно оргтехники")


my = Store()
my_p = Printer("laser")
my_s = Scanner("1440")
my_x = Xerox("40")
my_p2 = Printer("Matrix")
my.store_item = {my_p: 5}
my.store_item.update({my_s: 3})
my.add_to_store(my_x, 2)
my.add_to_store(my_p2, 20)

print(
    """
Оптимизация структуры данных задания 5 из урока 8 основ
Использую слоты в классах
"""
)

mem_usage = asizeof.asizeof(my) + asizeof.asizeof(my_p) + asizeof.asizeof(my_s) + asizeof.asizeof(
    my_x) + asizeof.asizeof(my_p2)
print("Без использования слотов объекты занимают в памяти: ", mem_usage)

my = StoreSlots()
my_p = PrinterSlots("laser")
my_s = ScannerSlots("1440")
my_x = XeroxSlots("40")
my_p2 = PrinterSlots("Matrix")
my.store_item = {my_p: 5}
my.store_item.update({my_s: 3})
my.add_to_store(my_x, 2)
my.add_to_store(my_p2, 20)

mem_usage = asizeof.asizeof(my) + asizeof.asizeof(my_p) + asizeof.asizeof(my_s) + asizeof.asizeof(
    my_x) + asizeof.asizeof(my_p2)
print("При использования слотов объекты занимают в памяти: ", mem_usage)

print(
    """
Даже в таком маленьком примере видна выгода, а если объектов будет в разы больше, как в реальном учете,
то будет достигнута существенная экономия памяти
"""
)
