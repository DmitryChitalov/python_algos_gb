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
from collections import deque


def standard(first, second, func='+'):  # подаются два 16-ричных числа в виде строк
    """Функция сложения, умножения двух 16-ричных цифр (для проверки результатов)"""
    if func == '+':
        result = hex(int(first, 16) + int(second, 16))
    elif func == '*':
        result = hex(int(first, 16) * int(second, 16))
    print('Эталон -> ', result)
    return result


def transform_16_1(elem):  # Подается строка
    """Функция преобразования 16-ричного объекта в 10-тичный"""
    n = 0
    elem = list(elem)
    for i in range(len(elem)):
        n += int(elem[i], 16) * (16 ** (len(elem) - i - 1))

    # n = sum(int(elem[i], 16) * (16 ** (len(elem) - i - 1)) for i in range(len(elem)))
    return n  # Десятичное число


def transform_16_2(elem, n=0):  # Подается объект deque
    """Функция преобразования 16-ричного объекта в 10-ричный. Рекурсия"""
    if len(elem) == 0:
        return n  # Десятичное число
    n = n + int(elem.popleft(), 16) * (16 ** (len(elem)))
    return transform_16_2(elem, n)


def summation16(first, second):
    result = str(hex(transform_16_2(first) + transform_16_2(second)))[2:]
    return result


def multiplication16(first, second):
    result = str(hex(transform_16_2(first) * transform_16_2(second)))[2:]
    return result


def cheсking():
    # 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
    print("Проверка работы функций, цель которых сложение и умножение 16-ричных чисел")

    a = input('Введите 16-ричное число ')
    b = input('Введите второе 16-ричное число ')
    a1 = deque(a)
    b1 = deque(b)
    print(f"\nСумма чисел {a} и {b} равна ", summation16(a1, b1))
    a1 = deque(a)
    b1 = deque(b)
    print(f"Произведение чисел {a} и {b}", multiplication16(a1, b1))
    print()

    standard(a, b)
    standard(a, b, '*')


# print(hex(4095))
# print(int('fff', 16), ' <- int')
# print(transform_16_1('fff'), ' <- transform_16_1')      # transform_16_1()
#
# c = deque('fff')                                        # transform_16_2()
# print(transform_16_2(c), '<- transform_16_2')


class Hex_number():
    def __init__(self, number):     # number -> 16-ичное число, строка
        self.number_16 = number
        self.numder_10 = sum(int(number[i], 16) * (16 ** (len(number) - i - 1)) for i in range(len(number)))

    def __add__(self, other):
        return Hex_number(str(hex(self.numder_10 + other.numder_10))[2:])

    def __mul__(self, other):
        return Hex_number(str(hex(self.numder_10 * other.numder_10))[2:])

    def __repr__(self):
        return self.number_16


def checking_class():
    print("Проверка работы класса обработки 16-ричных чисел")
    a, b = input("Введите 16-ричное число "), input("Введите второе 16-ричное число ")
    a16 = Hex_number(a)
    b16 = Hex_number(b)
    print('Сумма чисел -', (a16 + b16), "-, произведение -", (a16 * b16))


cheсking()
print("***")
checking_class()
