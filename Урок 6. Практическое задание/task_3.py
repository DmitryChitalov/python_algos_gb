"""
Задание 3.
Рекурсия
"""

from memory_profiler import profile
@profile
def factorial(arg):
    if arg ==1:
        return 1
    return arg*factorial(arg-1)


factorial(2)

from guppy import hpy

h = hpy()

y = deepcopy(x)
# @profile()
def recurs_sycle(b):
    if b == 0:
        return print('Программа закончила выпоолнение')
    print(b)
    return recurs_sycle(b -1)

recurs_sycle(5)

"""Анализ: Данный способ оценки использования памяти
  скорее всего использовать нельзя, потому что при профилировании проявляется то,
   что каждый запуск рекурсивной функции приводит к очередному запуску профилировки"""