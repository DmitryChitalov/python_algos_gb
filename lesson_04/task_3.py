"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from cProfile import run
from timeit import timeit
from random import randint


# использует рекурсию, имеет факториальную сложность
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# использует цикл, имеет линейную сложность
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# использует встроенную функцию и реверс среза имеет линейную сложность
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# тестовый массив чисел (6, 9 и 14 знаков)
array = (randint(100000, 999999), randint(100000000, 999999999), randint(10000000000000, 99999999999999))

# профилировка через cProfile

print('\nФункция revers:')
for number in array:
    run('revers(number)')

# Профилировка показывает, что в рекурсивной функции количество вызовов функции растёт вместе с длинной аргумента.
# При 6 знаках функция вызывается 7 раз, при 9 - 10, при 14 - 15.


print('\nФункция revers_2:')
for number_1 in array:
    run('revers_2(number_1)')

print('\nФункция revers_3:')
for number_2 in array:
    run('revers_3(number_2)')

# в функциях с циклом и срезом вызов функции всегда происходит один раз.

# Логично, что вторая и третья функции оптимальнее по времени, чем первая, ведь они не вызывают сами себя.
# Однако вызов происходит за одинаково малое время. Можно было бы запускать функции в цикле, но лучше для подсчёта
# скорости выполнения воспользуемся профилировкой через timeit.

# профилировка через timeit

print('\nФункция revers:')
for num in array:
    print(timeit('revers(num)', globals=globals(), number=10000))

print('\nФункция revers_2:')
for num_1 in array:
    print(timeit('revers_2(num_1)', globals=globals(), number=10000))

print('\nФункция revers_3:')
for num_2 in array:
    print(timeit('revers_3(num_2)', globals=globals(), number=10000))

# Замеры показывают, что самой быстрой оказалась функция со срезом (третья). Это обусловлено тем, что третья функция
# использует встроенную функцию str и встроенный функционал срезов, реализованные наиболее оптимальным образом.
# Кроме того, третья функция не тратит время на множество промежуточных вычислений и переприсваиваний,
# в отличие от функции с циклом. Рекурсивная же функция работает медленнее всего по определению - из-за
# сложности рекурсивного алгоритма.
