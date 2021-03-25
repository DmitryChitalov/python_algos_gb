"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import defaultdict

# Использовала defaultdict со списком по умолчанию для сохранения позиций элементов
# Переводила числа в десятичные поэлементно, затем складывала или умножала и
# переводила результат обратно в нужный формат с помощью рекурсивной функции


def from_string(number):
    """Переводит число в строковом формате в список"""
    return list(number)


def from_hex(number):
    """Переводит шестнадцатеричное число в виде списка в десятичное число"""
    num = defaultdict(list)
    number = number[::-1]
    for idx in range(len(number)):
        num[idx].append(number[idx])
    result = [int(elem, 16) * 16**key
              for key in num
              for elem in num[key]]
    return sum(result)


def to_hex(number, result=''):
    """Переводит десятичное число в шестнадцатеричное число в виде списка"""
    alphabet = '0123456789ABCDEF'
    if number == 0:
        return list(result)
    result = alphabet[number % 16] + result
    return to_hex(number // 16, result)


def add_numbers(num_1, num_2):
    """Складывает два шестнадцатеричных числа и возвращает результат в виде списка"""
    result = from_hex(num_1) + from_hex(num_2)
    return to_hex(result)


def mul_numbers(num_1, num_2):
    """Умножает два шестнадцатеричных числа и возвращает результат в виде списка"""
    result = from_hex(num_1) * from_hex(num_2)
    return to_hex(result)


if __name__ == '__main__':

    number_1 = from_string(input('Введите первое число: '))
    number_2 = from_string(input('Введите второе число: '))
    print(f'Числа теперь выглядят так: {number_1} и {number_2}')
    print(f'Сумма чисел: {add_numbers(number_1, number_2)}')
    print(f'Произведение чисел: {mul_numbers(number_1, number_2)}')
