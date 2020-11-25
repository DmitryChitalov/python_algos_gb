"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

import sys
from sympy import symbols, integrate, cos
from math import cos as cos1, pi
import scipy.integrate as sc
import numpy as np
import timeit



'''
Для оптимизации памяти и быстроты работы рекомендуется использовать следущее:
- использование форматирования строк вместо конкатенации
- избегать использование глобальных переменных
- использовать встроенные функции
- использование библиотек для конкретных задач

Те варианты которые мы уже разбирали я разбирать снова не буду.

Также для оптимизации можно трансляцию в Cython, интерпритатор PyPy, потоки и процессы
'''

'''
ПРИМЕР 1
(взят из интернета)
Использование __slots__. Позволяет "резервировать" атрибуты в классе, что уменьшает количество выделяемой памяти 
Но при этом добавлять новые атрибуты нельзя
В примере ф-я get_size считает количество выделенной памяти 
не используя __slots__ - 242
используя __slots__ - 28
'''
def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([get_size(v, seen) for v in obj.values()])
      size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
      size += sum([get_size(i, seen) for i in obj])
    return size

class DataItem(object):
    __slots__ = ['name', 'age', 'address']
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


d1 = DataItem("Alex", 42, "-")

print ("get_size(d1):", get_size(d1))

'''
ПРИМЕР 2
'''

'''
Использование библиотеки Numpy

В примерах ниже показано как на простых операциях вычисления  Numpy выигрывают по скорости по сравнению с стандартыми
функциями (по крайней мере в этих примерах)

func_1 и func_2 - суммирование всех элементов массива  
func_1 - 0.05910389999999999 
func_2 - 0.12757159999999995
func_3 и func_4 - умножение каждого элемента массива на 2
func_3 - 0.029345399999999966
func_4 - 1.0067766000000002
Как мы видим разница в скорости ощутима. 

Поэтому для выполнения операций с массивами чисел предпочтительней испольовать специальные библиотеки преднозначенные для 
этого
'''

def func_1():
    arr = np.arange(1, 1001)
    foo = arr.sum()
    return foo

def func_2():
    arr = list(range(1, 1001))
    foo = sum(arr)
    return foo

def func_3():
    arr = np.arange(1, 1001)
    foo = arr * 2
    return foo

def func_4():
    arr = list(range(1, 1001))
    foo = [i * 2 for i in arr]
    return foo


print(timeit.timeit('func_1()', setup="from __main__ import func_1", number=10000))
print(timeit.timeit('func_2()', setup="from __main__ import func_2", number=10000))
print(timeit.timeit('func_3()', setup="from __main__ import func_3", number=10000))
print(timeit.timeit('func_4()', setup="from __main__ import func_4", number=10000))

# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())
'''
ПРИМЕР 3
'''
'''
Использование библиотеки Sympy
(Взят из личного опыта)
Предположим нам нужно вычислить интеграл, возьмем cos(x) c пределами интегрирования от 1 до pi т.е
fun = cos1
fun_1 = cos(x)
a = 1
b = pi

Реализовывать интеграл будем методом треугольников, встроенной функцией Sympy и функцией в Scipy
причем cos(x) для Sympy будем брать из ее библиотеки

Получаем такие результаты:
Метод треугольников - -0.8413783305176771
Функция в Sympy - -0.8414709848078964
Функция в Scipy - -0.8414709848078964

Если округлить до нужной точности (0.0001) которую мы ввели в расчетах то результаты можно считать равными

Время выполнения (100 раз): 
Время выполнения Методом треугольников 0.6233091000000002
Время выполнения Функция в Sympy 1.3693476000000002
Время выполнения Функция в Scipy 0.0009588000000002594


Возьмем функцию f(x) = x**5 с пределами интегрирования 1 и 5
# fun = (lambda x: x**5)
# fun_1 = x**5   для Sympy
# a = 1
# b = 3

Получаем такие результаты (100 раз):
Метод треугольников - 121.30903771664975
Функция в Sympy - 121.33333333333333
Функция в Scipy - 121.33333333333333


В этом случае точность в методе треугольников оставляет желать лучшего

Время выполнения: 
Время выполнения Методом треугольников 0.9351454000000001
Время выполнения Функция в Sympy 0.5045718999999993
Время выполнения Функция в Scipy 0.0012190000000007473

Как мы видим из полученых результатов библиотечные функции лучше самописных
Возможно метод расчета интеграла выбран не самый удачный или реализация подкачала, но библиотечные ф-и лучше))
'''
x = symbols('x')
# fun = cos1
# fun_1 = cos(x)
# a = 1
# b = pi
fun = (lambda x: x**5)
fun_1 = x**5
a = 1
b = 3


def trap(f,a,b,h):
    s=0.5*(f(a)+f(b))
    x=a+h
    while (x<=b-h):
        s+=f(x)
        x+=h
    return h*s


def inter(f,a,b):
    foo = integrate(f, (x, a, b))
    return foo


def inter_sc(f,a,b):
    i = sc.quad(f, a, b)
    return i


print(f'Метод треугольников - {float(trap(fun, a, b, 0.0001))}')
print(f'Функция в Sympy - {float(inter(fun_1,a, b))}')
print(f'Функция в Scipy - {inter_sc(fun,a, b)[0]}')

print(f"Время выполнения Методом треугольников "
      f"{timeit.timeit('(trap(fun, a, b, 0.0001))', setup='from __main__ import trap ,fun,a,b', number=100)}")
print(f"Время выполнения Функция в Sympy "
      f"{timeit.timeit('inter(fun_1,a, b)', setup='from __main__ import inter, fun_1,a,b', number=100)}")
print(f"Время выполнения Функция в Scipy "
      f"{timeit.timeit('inter_sc(fun,a, b)[0]', setup='from __main__ import inter_sc, fun,a,b', number=100)}")

'''
Пример 4
Pypy

Реализацию этого примера я делал на linux
Возьмем код:
arr = list(range(1, 20000001))
foo = sum(arr)
foo1 = [i * 2 for i in arr]
print(foo)

Запустим его c помощью python и замерим скорость его работы с помощью встроенного в linux time
        grimo@ubuntu:~/python$ time python3 1.py
        200000010000000
        
        real	0m2,603s
        user	0m2,014s
        sys	    0m0,579s
Теперь запустим тот же самый код но с Pypy
        grimo@ubuntu:~/python$ time ./pypy3.7-v7.3.3-linux64/bin/pypy 1.py
        200000010000000
        
        real	0m0,331s
        user	0m0,154s
        sys	    0m0,174s

Python 3.7.9 и [PyPy 7.3.3-beta0 with GCC 7.3.1 20180303 (Red Hat 7.3.1-5) если это важно
Как видим результат на лицо))

'''