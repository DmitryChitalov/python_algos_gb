"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def count_even_odd(number):
    if number >= 10:
        if number % 2 == 0:
            a, b = count_even_odd(number // 10)
            return a + 1, b
        else:
            a, b = count_even_odd(number // 10)
            return a, b + 1
    else:
        if number % 2 == 0:
            return 1, 0
        else:
            return 0, 1


def count_even_odd2(number):  # чуть короче
    if number >= 10:
        a, b = count_even_odd2(number // 10)
        return a + int(number % 2 == 0), b + number % 2
    else:
        if number % 2 == 0:
            return 1, 0
        else:
            return 0, 1


if __name__ == '__main__':
    print(f'Количество четных и нечетных цифр в числе равно: {count_even_odd(123)}')
    print(f'Количество четных и нечетных цифр в числе равно: {count_even_odd2(10100909)}')
