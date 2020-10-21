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


from random import randint


###################################
# Поиск простых чисел
def simple(i):
    """Без использования «Решета Эратосфена»
    Сложность: O(4n**2 + 5n + 2)
    """
    count = 1                                       # O(1)
    n = 2                                           # O(1)
    while count <= i:                               # O(n * (4n + 5)) = O(4n**2 + 5n)
        t = 1                                       # O(1)
        is_simple = True                            # O(1)
        while t <= n:                               # O(4n)
            if n % t == 0 and t != 1 and t != n:    # O(3)
                is_simple = False                   # O(1)
                break
            t += 1                                  # O(1)
        if is_simple:                               # O(2)
            if count == i:                          # O(1)
                break
            count += 1                              # O(1)
        n += 1                                      # O(1)
    return n


def simple_eratosfen(i):
    """Функция поиска i-го элемента в ряде простых чисел.
    Используется алгоритм Решето Эратосфена.

    Сложность: O(n**2 + 3n + 5)

    :param i: порядковый номер искомого элемента в ряде
    :return: Возвращает i-й элемент ряда простых чисел
    """
    simples = [2]                       # O(1)
    n = simples[len(simples) - 1] + 1   # O(3)
    while len(simples) < i:             # O(1 + n * (n + 3)) = O(n**2 + 3n + 1)
        is_simple = True                # O(1)
        for s in simples:               # O(n)
            if n % s == 0:              # O(1)
                is_simple = False       # O(1)
                break
        if is_simple:                   # O(1)
            simples.append(n)           # O(1)
        n += 1                          # O(1)
    return simples[len(simples) - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

print(simple_eratosfen(i))


###################################
# Реверс случайного большого числа
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return ''
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        num = f"{num}{revers(enter_num, revers_num)}"
    return num


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num_10000 = randint(100000000, 10000000000000)
print(f"Исходное число: {num_10000}")

print(f"revers: {revers(num_10000)}")
print(f"revers_2: {revers_2(num_10000)}")
print(f"revers_3: {revers_3(num_10000)}")
print()


