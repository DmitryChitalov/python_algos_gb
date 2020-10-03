"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import profile
import sys
import collections
import recordclass

# Использование пустых кортежей вместо пустых списков. Пустые кортежи ссылаются на один и тот же объект, а
# списки - нет.


@profile
def my_func_1():
    a = ()
    b = ()
    c = ()
    print(a)


@profile
def my_func_2():
    a = [i for i in range(100)]
    b = []
    c = []
    print(a)


my_func_1()
my_func_2()

# 2
# Исползовать колличество значений, которые соответствуют свободным ячейкам в списках. Пайтон добавляет скрытые ячейки
# в списки, которые не видны пользователю по формуле: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88
#
# 3
# Использование класса вместо словаря


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(sys.getsizeof(my_dict))


class MyClass:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


my_object = MyClass(1, 2, 3)
print(sys.getsizeof(my_object))


# 4
# Кортежи занимают меньше памяти, чем списки
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(sys.getsizeof(my_list), sys.getsizeof(my_tuple))

# 5
# Использование namedtuple вместо словаря.
a = collections.namedtuple('nums', 'a b c')
c = a(a=1, b=2, c=3)
my_dict_2 = {'a': 1, 'b': 2, 'c': 3}
print(sys.getsizeof(c), sys.getsizeof(my_dict_2))

# 6
# Использование Recordclass. Даже более эффективно, чем namedtuple
Point = recordclass.recordclass('nums', 'a b c')
ob = Point(1, 2, 3)
print(sys.getsizeof(ob), sys.getsizeof(my_dict_2))

# 7
# Использование Dataobject. Даже более эффективно, чем Recordclass
Point_2 = recordclass.make_dataclass('nums', 'a b c')
ob_2 = Point_2(1, 2, 3)
print(sys.getsizeof(ob_2), sys.getsizeof(my_dict_2))

