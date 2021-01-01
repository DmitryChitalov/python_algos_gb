"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit

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


sample_num = 123456789123456789
print(sample_num)


def main():
    for i in range(1000):
        revers(sample_num)
        revers_2(sample_num)
        revers_3(sample_num)


cProfile.run('main()')

print(timeit("revers(sample_num)", setup="from __main__ import sample_num, revers", number=1000))
print(timeit("revers_2(sample_num)", setup="from __main__ import sample_num, revers_2", number=1000))
print(timeit("revers_3(sample_num)", setup="from __main__ import sample_num, revers_3", number=1000))


"""
Время выполнения функций (1000 повторений):

revers:     0.0040678 сек
revers_2:   0.0026879 сек
revers_3:   0.0003335 сек

Эффективнее всего выполняется функция revers_3.
Функции revers и revers_2 выполняют деление, поэтому выполняются дольше, чем revers_3, которая работает со строковыми 
символами по индексу. Функция revers выполняется дольше всего, т.к. использует рекурсию, а рекурсия добавляет расходы
на работу со стэком.
"""
