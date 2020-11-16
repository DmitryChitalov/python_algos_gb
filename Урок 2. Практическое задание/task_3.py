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


def mirror_func(user_number, num_rev = 0):

    if user_number == 0:
        return num_rev
    else:
        num_last = user_number % 10
        num_rev = num_rev * 10 + num_last
        user_number = user_number // 10
        return mirror_func(user_number, num_rev)

try:
    user_number = int(input('Enter your number: '))
    print(f'Your reverse number is: {mirror_func(user_number)}')
except ValueError:
    print('Try an integer instead!')
