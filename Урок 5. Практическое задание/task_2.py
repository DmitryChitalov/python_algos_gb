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

import collections

hex_dec = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B',
    '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

# с использованием модуля collections
num1 = list(input('Введите первое шестнадцатеричное число: ').upper())
num2 = list(input('Введите второе шестнадцатеричное число: ').upper())
dec1 = collections.deque(num1)
dec2 = collections.deque(num2)

# преобразуем шестнадцатеричные значения с конца каждого дека в десятичные числа и вставляем их в начало дека
for i in range(len(dec1)):
    dec1.appendleft(int(list(hex_dec.keys())[list(hex_dec.values()).index(dec1.pop())]) * (16 ** i))
for i in range(len(dec2)):
    dec2.appendleft(int(list(hex_dec.keys())[list(hex_dec.values()).index(dec2.pop())]) * (16 ** i))

dec_num1 = sum(dec1)  # первое число в десятичной форме
dec_num2 = sum(dec2)  # второе число в десятичной форме
sum_dec = dec_num1 + dec_num2  # результат сложения в десятичной форме
mul_dec = dec_num1 * dec_num2  # результат умножения в десятичной форме


def get_hex(dec_number):
    """"""
    arr = []
    while dec_number > 0:
        res = dec_number % 16
        arr.insert(0, hex_dec[str(res)])
        dec_number = dec_number // 16
    return arr


print('Результаты с использованием deque методов:')
print(f'Сумма чисел: {"".join(get_hex(sum_dec))}')
print(f'Произведение чисел: {"".join(get_hex(mul_dec))}')
print('-' * 160)


# через ООП с перегрузкой методов
class Number:
    def __init__(self, x):
        self.x = int(''.join(x), 16)

    def __add__(self, other):
        """Перегружает сложение"""
        return f'Сумма чисел: {str(hex(self.x + other.x))[2:].upper()}'

    def __mul__(self, other):
        """Перегружает умножение"""
        return f'Произведение чисел: {str(hex(self.x * other.x))[2:].upper()}'


num3 = Number(list(input('Введите первое шестнадцатеричное число: ')))
num4 = Number(list(input('Введите второе шестнадцатеричное число: ')))
print('Результаты с использованием перегруженных методов:')
print(num3 + num4)
print(num3 * num4)
