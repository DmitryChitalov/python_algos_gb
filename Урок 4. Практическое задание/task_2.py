"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

fimport timeit

def memorize(func):
    def g(number, memory={}):
        r = memory.get(number)
        if r is None:
            r = func(number)
            memory[number] = r
        return r
    return g


@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

number=453
print(timeit.timeit('recursive_reverse(number)', setup="from __main__ import recursive_reverse,number"))
"""
я использовала мемортзатион что бы каждый раз при вызове рекурсии она не вычеслялась с однтмт теми же параметрамии при этом секаномит время"""