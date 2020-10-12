"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
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


def check_math_induction(n, print_it=False):
    """Функция, доказывающая справедливость метода математической индукции

    :param n: Число до кторого строить ряд от 1
    :param print_it: Признак выводить ли результаты вычислений
    :return: Возвращает признак Boolean доказывающий метод
    """
    m = int(n * (n + 1) / 2)
    if print_it:
        print(f"при n={n}: n * (n + 1) / 2 = {m}")
    n = math_induction(n, print_it)
    if print_it:
        print(f" = {n}")
    if print_it:
        print(f"Равны? {m == n}")
    return m == n


################################
print(math_induction(4))
print(check_math_induction(15))
check_math_induction(15, True)
