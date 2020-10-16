"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile
input_num = int(input("Введите число для реверсa: "))


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


print(timeit.timeit("revers(input_num)", setup="from __main__ import revers, input_num", number=1000))
print(timeit.timeit("revers_2(input_num)", setup="from __main__ import revers_2, input_num", number=1000))
print(timeit.timeit("revers_3(input_num)", setup="from __main__ import revers_3, input_num", number=1000))
cProfile.run('revers(input_num)')
cProfile.run('revers_2(input_num)')
cProfile.run('revers_3(input_num)')

"""
через timeit видно что самый медленный вариант первый, самый быстрый второй. В первом применена рекурсия, многократный
вызов замедляет работу программы, а так же математические операции. Во втором случае применен цикл while, вместо
рекурсии. В остальном код схож. В третьем математических операций нет. Входное число приводится к типу строка, делается
срез, возвращается результат. Код краток
через cProfile из за однократного вызова скорость сравнить не удается, удается только увидеть многократный рекурсивный 
вызов в первом варианте
"""