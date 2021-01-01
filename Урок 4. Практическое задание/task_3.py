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

#Рекурсия по скорости выполнения всегда уступает циклу
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

# Цикл в данном случае уступает по скорости срезу строки так,
# как имеет арифметические действия
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num



# Строка(срез) самый быстрый из данных способ решения данной задачи так,
# как уступает рекусии с мемоизацией из предыдущей задачи
#0,0045 против 0.00269
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

num_100 = randint(10000, 1000000)

print('Замеры модулем timeit')
print('Рекурсия')
print(
    timeit(
        "revers(num_100)",
        setup='from __main__ import revers, num_100',
        number=10000))
print('Цикл')
print(
    timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=10000))
print('Строка(срез)')
print(
    timeit(
        "revers_3(num_100)",
        setup='from __main__ import revers_3, num_100',
        number=10000))

print('Замеры модулем timeit')
print('Рекурсия')
cProfile.run('revers(num_100)')
print('Цикл')
cProfile.run('revers_2(num_100)')
print('Строка')
cProfile.run('revers_3(num_100)')