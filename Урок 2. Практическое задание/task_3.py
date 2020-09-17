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

from task_2 import input_number


def revers_num(num):
    """
    функция получает натуральное число, рекурсивно извлекает цифры и складывает их в обратном порядке
    возвращяет число
    """
    digit = num % 10
    if num // 10 == 0:
        return digit
    return int(str(digit) + str(revers_num(num // 10)))


if __name__ == '__main__':
    print(revers_num(input_number()))
