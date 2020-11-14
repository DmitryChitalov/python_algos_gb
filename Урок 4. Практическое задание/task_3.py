"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile
from random import randint

num = randint(1000000, 9999999)


# из любопытства попытка изменить эфффективность revers_2 при помощи мемоизации
# (декоратор закомментирован изначально)
def memorize(func):
    def wrapper(enter_num, revers_num=0, mem={}):
        r = mem.get(enter_num)
        if r is None:
            r = func(enter_num, revers_num)
            mem[enter_num] = r
        return r

    return wrapper


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# @memorize
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Функция revers:', end=' ')
print(timeit('revers(num)', setup='from __main__ import revers, num', number=10000))

print('Функция revers_2:', end=' ')
print(timeit('revers_2(num)', setup='from __main__ import revers_2, num', number=10000))

print('Функция revers_3:', end=' ')
print(timeit('revers_3(num)', setup='from __main__ import revers_3, num', number=10000))

print(f'\nПрофилирование:\n')
print('Функция revers:')
cProfile.run('revers(num)')
print('Функция revers_2:')
cProfile.run('revers_2(num)')
print('Функция revers_3:')
cProfile.run('revers_3(num)')

'''
Первые две функции используют математический метод вычисления цифры-символа для перестановки
его в начало.
 
Первая функция выполняется дольше всего из-за применения механизма рекурсии (без мемоизации),
и вызывает саму себя несколько раз, что отображено в профилировании;

вторая функция выполняет цикл while внутри себя и работает на треть быстрее первой;

третья использует встроенный метод переворачивания строки при помощи отрицательного
шага среза, поэтому скорость её выполнения быстрее предыдущих функций.

Их трёх предложенных функций - reverse_3 эффективнее по скорости выполнения и краткости
написания кода.

Если применить мемоизацию к reverse_2 - она будет быстрее по выполнению, чем остальные.

'''
