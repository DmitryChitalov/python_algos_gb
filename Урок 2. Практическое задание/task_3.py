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


def expand(numb, expand_numb=''):
    if numb == '':
        return print(f"Перевернутое число:: ({expand_numb})")
    else:
        numb_str = str(numb)
        expand_numb = expand_numb + numb_str[-1]
        return expand(numb_str[:-1], expand_numb)


# Так же не стал делать проверку на число так как в задании нет такого требования

expand(int(input("Введите число, которое требуется перевернуть: ")))
