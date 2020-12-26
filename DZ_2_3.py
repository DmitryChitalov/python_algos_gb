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
# Я нашел очень простое решение с помощью опять же того среза который был представлен в примере.
# Просто. Красиво. Лаконично. Ноль - полноценный участник сего действия!


def recurs(lst_obj):
    if len(lst_obj) == 1:
        return lst_obj[0]
    else:
        return str(recurs(lst_obj[1:])) + str(lst_obj[0])


user_input = (input("Введите число которое нужно перевернуть: "))
while not user_input.isdigit():
    user_input = (input("Нужно ввести число! Введите число которое нужно перевернуть: "))
print(f"Получаем число в обратную сторону {recurs([int(i) for i in list(str(user_input))])}")
