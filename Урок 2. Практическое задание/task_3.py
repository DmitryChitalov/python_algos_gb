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


def num_reverse_1(num, list_items):
    str_num = str(num)
    item_in_num = str_num[len(str_num) - 1]
    list_items.append(item_in_num)
    if len(str_num) == 1:
        print(int(''.join(list_items)))
        return
    else:
        num_reverse_1(num // 10, list_items)


def num_reverse_2(num, new_num=0):
    item = num % 10
    new_num *= 10
    new_num += item
    if len(str(num)) == 1:
        print(new_num)
        return
    else:
        num_reverse_2(num // 10, new_num)


if __name__ == "__main__":
    list_items = []
    num_reverse_1(123456789, list_items)
    num_reverse_2(2345)
