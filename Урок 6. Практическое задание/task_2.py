"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile, memory_usage
import struct
from pympler import asizeof
import time
import gc

#  предложил только не используемые на лекции варианты
#  1. Используем встроенный модуль struct для упаковки и распаковывания данных
"""
Исользование модуля struct дает выигрыш в памяти при хранении данных (например экземпляров класс). В примере ниже
в class StructPolygon мы сохраняем все данные экземпляра класс в одном объекте ('_data',) (используя __slots__), а 
не храним их в шести отдельных, как в class StandardPolygon. Таким образом для данного примера (если упаковываем
данные в байты используя short integer) получаем выигрыш по памяти в 7 раз (56 байт для экземпляра StructPolygon
против 392 байт для экземпляра StandardPolygon).
"""


class StandardPolygon:
    """Обычный класс"""

    def __init__(self, x1, y1, x2, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2


polygon1 = StandardPolygon(5, 6, 8, 10, 4, 9)
print(polygon1.__dict__)
print(asizeof.asizeof(polygon1))


class StructPolygon:
    """используем slots и struct"""

    __slots__ = ('_data',)  # выделяем под будущий экземпляр класса один object (StructPolygon._data)
    Coords = struct.Struct('hhhhhh')  # Struct object, упаковываем в short integer (используем class struct.Struct)

    # Coords = struct.Struct('llllll')  # Struct object, упаковываем в long integer

    def __init__(self, x1, y1, x2, y2, z1, z2):
        self._data = StructPolygon.Coords.pack(x1, y1, x2, y2, z1, z2)  # упаковываем наши координаты в байты

    @property
    def x1(self):
        return StructPolygon.Coords.unpack(self._data)[0]

    @property
    def x2(self):
        return StructPolygon.Coords.unpack(self._data)[1]

    @property
    def y1(self):
        return StructPolygon.Coords.unpack(self._data)[2]

    @property
    def y2(self):
        return StructPolygon.Coords.unpack(self._data)[3]

    @property
    def z1(self):
        return StructPolygon.Coords.unpack(self._data)[4]

    @property
    def z2(self):
        return StructPolygon.Coords.unpack(self._data)[5]


polygon2 = StructPolygon(5, 6, 8, 10, 4, 9)
print(asizeof.asizeof(polygon2))

#  2. Используем встроенное форматирование строк вместо конкатенации
"""
Во многих источниках прочитал, что выигрыш в использовании памяти дает использование форматированной строки вместо
конкатенации, так как не происходит аллокация памяти под временные строки, когда поочередно конкатенируем строки.
Попробовал проверить в коде. Выигрыш есть, но совсем небольшой (0.1 MiB для моего примера). Возможно, имеет смысл 
задумываться над этим только когда число конкатенируемых строк очень большое, тогда выигрыш будет ощутимым.
"""


@profile
def format_str(a, b, c, d, e):
    res = f'{a}_{b}_{c}_{d}_{e}_{a}_{b}_{c}_{d}_{a}_{b}'
    return res


@profile
def concat_str(a, b, c, d, e):
    res = (a + '_' + b + '_' + c + '_' + d + '_' + e + '_' + a + '_' + b + '_' + c + '_' + d + '_' + a + '_' + b)
    return res


concat_str('one' * (10 ** 4), 'two' * (10 ** 3), 'three' * (10 ** 3), 'four' * (10 ** 3), 'five' * (10 ** 3))
format_str('one' * (10 ** 4), 'two' * (10 ** 3), 'three' * (10 ** 3), 'four' * (10 ** 3), 'five' * (10 ** 3))

#  3. Используем memoryview()
"""
Используя memoryview, можем делать срезы очень больших данных без копирования исходных данных. Memoryview поддерживает 
срезы. Таким образом этот тип подходит, когда нужно очень много срезов на одних бинарных данных. Memoryview объекты 
позволяют обращаться к внутренним данным объекта, который поддерживает protocol buffer и работать с этими данными без 
копирования
"""


def mem_usage_decorator(some_func):
    """Вычисляет память, выделяемую под выполнение декорируемой функции"""

    def wrapper(*args, **kwargs):
        print(f'Задействованная память до запуска функции: {str(memory_usage())} MB')
        result = some_func(*args, **kwargs)
        print(f'Задействованная память после запуска функции: {str(memory_usage())} MB')

        return result

    return wrapper


@mem_usage_decorator
def usual_slice():
    for n in (100000, 200000, 300000, 400000):
        data = bytes(n)
        start = time.time()
        b = data
        while b:
            b = b[1:]
        print('bytes', n, time.time() - start)


@mem_usage_decorator
def mem_view_slice():
    for n in (100000, 200000, 300000, 400000):
        data = bytes(n)
        start = time.time()
        b = memoryview(data)  # не создаем отдельной копии для срезов
        while b:
            b = b[1:]
        print('memoryview', n, time.time() - start)


usual_slice()
print(f'GC collected objects : {gc.collect()}')
print('-' * 160)
mem_view_slice()
