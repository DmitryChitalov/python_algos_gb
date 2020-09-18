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


def get_reverse_number(user_number, result_list=[]):
    user_list = list(str(user_number))
    if len(user_list) == 1:
        number = user_list.pop()
        result_list.append(number)
        result = int(''.join(result_list))
        print(f'Перевернутое число = {result}')
    else:
        number = user_list.pop()
        result_list.append(number)
        temp_list = int(''.join(user_list))
        get_reverse_number(temp_list, result_list)


get_reverse_number(user_number=input('Введите число: '))