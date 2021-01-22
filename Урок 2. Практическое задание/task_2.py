"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def count_evn(number, count_even=0, count_uneven=0):
    """
    Функция считает четные и нечетные цифры в натуральном числе
    :param number:
    :param count_even:
    :param count_uneven:
    :return:
    """

    if not number:
        return print(f'Количество четных и нечетных цифр в числе равно: ({count_even}, {count_uneven})')
    # n = number % 10
    n, d = divmod(number, 10)
    if d % 2 != 0:
        count_even += 1
    else:
        count_uneven += 1
    return count_evn(n, count_even, count_uneven)


num = int(input('Введите натуральное число: '))
count_evn(num)
