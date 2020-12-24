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


def reversion_2(numb, reversed_numb=0):
    try:
        if numb == 0:
            return reversed_numb
        else:
            return reversion_2(numb // 10, reversed_numb * 10 + numb % 10)
    except TypeError:
        print('Вы ввели не строку')


# Решение через строку
def reversion(number, reversed_number=''):
    if len(str(number)) == 0:
        return reversed_number
    else:
        return reversion(str(number)[:-1], reversed_number + str(number)[-1])


print(reversion(12345))
print(reversion_2(12345))
