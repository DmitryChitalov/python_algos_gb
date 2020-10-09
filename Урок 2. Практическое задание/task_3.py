#! /bin/python3
"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def reverse_n(n):
    """
    Переворачиваем число как 'число', т.е. если в конце были нули,
    то после переворота они становятся ведущими и отбрасываются
    """
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_n(n // 10)))


def reverse_s(n):
    """
    Переворачиваем число как строку,
    т.е. ведущие нули сохранятся в результате
    """
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + reverse_s(n // 10)


num = int(input('Введите целое число: '))
print(reverse_n(num))
print(reverse_s(num))
