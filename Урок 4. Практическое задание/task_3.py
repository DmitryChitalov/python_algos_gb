"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import repeat
from cProfile import run

number = int(input('Введите число. '))


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


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


print('***********Первая функция.***********')

print(
    min(repeat(
        'revers(number)',
        globals=globals(),
        repeat=3,
        number=10000)))

run('revers(number)')

print('***********Вторая функция.***********')
print(
    min(repeat(
        'revers_2(number)',
        globals=globals(),
        repeat=3,
        number=10000)))

run('revers_2(number)')

print('***********Третья функция.***********')
print(
    min(repeat(
        'revers_3(number)',
        globals=globals(),
        repeat=3,
        number=10000)))
run('revers_3(number)')

"""Выводы: поскольку первый алгоритм - рекурсия, реализованная без мемоизации, то это самый затратный алгоритм, на что
нам указывает timeit для его выполнения, а также количество вызовов функции cProfile (у всех результат по 0.000 в 
cProfile, так как (по моему мнению) они выполняются быстрее, чем за 0,0005 секунд) а самая эффективная (как раз вспомнил
номер из первого дз) это функция revers_3 так как в ней используется всего одна встроенная функция для списка, а именно
срез, имеющая сложность O(1), а также присваивание, тоже O(1)"""
