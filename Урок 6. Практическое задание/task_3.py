"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""


from random import randint
from memory_profiler import profile

"""
Для профилировки памяти рекурсивной функции буду использовать задачу 2 с урока 4.

Естественно, если профилировать именно рекурсивную функцию,
то при каждом рекурсивном запуске функции будет в очередной раз инициироваться новый профайлер.
По-этому для профилирования рекурсивной функции нужно профайлер добавить на функцию,
которая будет вызывать рекурсивную функцию.  
"""


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@profile
def recursive_reverse__profile(number):
    return recursive_reverse(number)


num_10000 = randint(100000000, 10000000000000)

# Вывод исходного числа
print(num_10000)
# Вывод реверсивного числа
print(recursive_reverse(num_10000))
# Вывод реверсивного числа с выводом профилирования памяти
print(recursive_reverse__profile(num_10000))


######################################
"""
Вот еще пример реверсивной функции из задачи 7 урока 2.
Суммирование ряда от 1 до n
"""


def math_induction(n, print_it=False):
    """Рекурсивная функция суммирования ряда чисел от 1 до n

    :param n: Число, до которого суммировать ряд
    :param print_it: Признак нужен ли вывод ряда в терминал
    :return: Возвращает сумму ряда от 1 до n
    """
    if n == 1:
        if print_it:
            print(n, end="")
        return n
    m = math_induction(n - 1, print_it)
    if print_it:
        print(f"{' + ' if n > 1 else ''}{n}", end="")
    return n + m


@profile
def math_induction_profile(n, print_it=False):
    return math_induction(n, print_it)


print("\nСуммирование ряда")
num = 990
print(f"Сумма ряда от 1 до {num} = {math_induction_profile(num)}")

"""
Вывод:
Если нужно профилировать память для рекурсивных функций, то есть 2 варианта:
    1. Завернуть рекурсивную функцию в родительскую с декоратором @profile,
        но тогда к рекурсивной функции не будет глобального доступа;
    2. Осуществлять профилирование рекурсивной функции из отдельной функции с декоратором @profile.
"""
