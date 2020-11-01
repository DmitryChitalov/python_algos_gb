"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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


if __name__ == '__main__':
    num = 1042546
    import cProfile
    from timeit import timeit, repeat, default_timer

    cProfile.run('revers(num, revers_num=0)')
    cProfile.run('revers_2(num, revers_num=0)')
    cProfile.run('revers_3(num)')

    print('Время выполнения варианта с рекурсией: ', end='')
    print(
        timeit(
            "revers(num, revers_num=0)",
            setup='from __main__ import revers, num',
            number=10000))

    print('Время выполнения варианта с циклом: ', end='')
    print(
        timeit(
            "revers_2(num, revers_num=0)",
            setup='from __main__ import revers_2, num',
            number=10000))

    print('Время выполнения варианта со срезом: ', end='')
    print(
        timeit(
            "revers_3(num)",
            setup='from __main__ import revers_3, num',
            number=10000))

"""
Самым эффективным вариантом является вариан с использованием среза, так как он имеет сложность О(n) и это встроенный
механизм.
Вариант с циклом работает медленнее, так как, имея тоже линейную сложность, он также выполняет дополнительные
вычисления и присваивания переменным.
Вариант с рекурсией самый медленный из-за необходимости организации стека вызовов, в котором каждая функция выполняет
вычисления и возвращает результат предыдущему вызову в стеке.
"""
#  для сравнения timeit и repeat
setup = """
from __main__ import revers, revers_2, revers_3, num
"""
statements = [
    ['Время выполнения варианта с рекурсией: ', 'revers(num, revers_num=0)'],
    ['Время выполнения варианта с циклом: ', 'revers_2(num, revers_num=0)'],
    ['Время выполнения варианта со срезом: ', 'revers_3(num)']
]
print('-' * 120)
for info, st in statements:
    print(info, max(repeat(st, setup, default_timer, 3, 10000)))
