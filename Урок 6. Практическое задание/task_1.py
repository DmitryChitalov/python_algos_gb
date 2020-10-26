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


# 1
class ComplexDigit:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)


class Calculator:
    @profile()
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        print(ComplexDigit(real, imag))

    @profile()
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        print(ComplexDigit(real, imag))


calc = Calculator
a = ComplexDigit(1, 3)
b = ComplexDigit(2, -4)

calc.__add__(a, b)  # профилирование памяти в данном методе класса - по нолям. Сам профайлер - 18.8 MiB

calc.__mul__(a, b)  # профилирование памяти в 'njv методе класса - тоже по нолям. Профайлер - 18.8 MiB, без искажения.

# 2
array = [1, 3, 1, 3, 4, 5, 1]


@profile
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())  # Инкремент в обоих функциях - нолевой. профайлер 18.8


# 3

@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


recursive_reverse(1234567898765432123456)  # И вновь по нолям инкремент, профайлер 18.9.


# 4

@profile
def func():
    e = [i for i in range(1000000)]
    d = e
    return d

func() #  В этой ф-ии при создании списка генераторным выражением - затраты память составили 30.9,
# помимо 18.9 на профайлер.


# Были проанализирваны три функции, но увы, инкремент нолевой, видимо слишком простые ф-ии. При использовании профайлера,
# была замечена незначительная погрешность d 0,1 MiB .
# Python 3.8, 64-разрадная
