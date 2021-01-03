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


def relocate(n):
    n_list.append(n % 10)
    n = n // 10
    if n > 0.1:
        return relocate(n)
    new_num = ''.join(map(str, n_list))
    return f'Ваше число наоборот выглядит так {new_num}'




    # return len(n), l, n_list
    # if l > 0:
    #     return relocate(n)
    # return n_list


n = int(input('Введите любое натуральное число: _'))
n_list = []
print(relocate(n))




