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

reverse_number = []


def reverse(number):
    if len(number) == 1:
        reverse_number.append(number[0])
        stroka = "".join(reverse_number)
        #print("Перевернутое число:")
        return f'Перевернутое число:{stroka}'

    reverse_number.append(number[-1])
    return reverse(number[0:len(number) - 1])


print(reverse(input("Введите число:")))


"""Этот вариант не очень удался..."""
# def rev(n, r=0):
#
#     if n <= 0:
#         return str(n)
#     else:
#         r = n % 10
#         n = n // 10
#     return f'{str(r)}{rev(n)}'
#
#
# print(rev(int(input("Введите число:"))))
