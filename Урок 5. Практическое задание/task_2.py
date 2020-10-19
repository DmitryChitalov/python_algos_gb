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

from collections import deque, Counter
from functools import reduce


a_hex = 'A2'
b_hex = 'C4F'
hex_base = '0123456789ABCDEF'


class HexNum:

    __hex_base = '0123456789ABCDEF'
    
    def __init__(self, hex_num):
        self.hex_num = deque(str(hex_num))
    
    @property
    def hexnum(self):
        return list(self.hex_num)
    
    @property
    def decnum(self):
        return int(str(self), 16)

    def __summ_hex(self, a, b):
        c = deque()
        overflow = 0
        while len(a) > 0 or len(b) > 0:
            num_a = int(a.pop(), 16) if len(a) > 0 else 0
            num_b = int(b.pop(), 16) if len(b) > 0 else 0
            n = num_a + num_b + overflow
            c.appendleft(self.__hex_base[n % len(self.__hex_base)])
            overflow = n // len(self.__hex_base)
        if overflow > 0:
            c.appendleft(self.__hex_base[overflow])
        return c
    
    def __str__(self):
        return ''.join(self.hex_num)
    
    def __add__(self, b):
        a = self.hex_num.copy()
        b = b.hex_num.copy()
        return HexNum(''.join(self.__summ_hex(a, b)))
    
    def __mul__(self, b):
        a = self.hex_num.copy()
        b = b.hex_num.copy()
        c = deque()
        level = ''
        while len(a) > 0:
            overflow = 0
            num_a = int(a.pop(), 16) if len(a) > 0 else 0
            b2 = b.copy()
            c2 = deque(level)
            while len(b2) > 0:
                num_b = int(b2.pop(), 16) if len(b2) > 0 else 0
                n = num_a * num_b + overflow
                c2.appendleft(self.__hex_base[n % len(self.__hex_base)])
                overflow = n // len(self.__hex_base)
            if overflow > 0:
                c2.appendleft(self.__hex_base[overflow])
            c.appendleft(c2)
            level += '0'
        return HexNum(''.join(reduce(self.__summ_hex, c)))


##################################
print("\nООП:")
a = HexNum(a_hex)
b = HexNum(b_hex)

print(f"{a} = {a.decnum}")
print(f"{b} = {b.decnum}")

c = a + b
print(f"{a} + {b} = {c}")

d = a * b
print(f"{a} * {b} = {d}")


##################################
def sum_hex(source_a, source_b):
    """
    Функция суммирует шестнадцатиричные числа, которые представлены в виде очереди deque

    :param source_a: Очередь числа a
    :param source_b: Очередь числа b
    :return: Возвращает очередь deque суммы 2-х входящих чисел
    """
    a = source_a.copy()
    b = source_b.copy()
    c = deque()
    overflow = 0
    while len(a) > 0 or len(b) > 0:
        dec_a = int(a.pop(), 16) if len(a) > 0 else 0
        dec_b = int(b.pop(), 16) if len(b) > 0 else 0
        n = dec_a + dec_b + overflow
        c.appendleft(hex_base[n % len(hex_base)])
        overflow = n // len(hex_base)
    if overflow > 0:
        c.appendleft(hex_base[overflow])
    return c


def mul_hex(source_a, source_b):
    """
    Функция умножает 2 шестнадцатиричных числа, представленных в виде очереди цифр

    :param source_a: Очередь числа a
    :param source_b: Очередь числа b
    :return: Возвращает пролизведение чисел a и b в виде очереди чисел deque
    """
    a = source_a.copy()
    b = source_b.copy()
    c = deque()
    level = ''
    while len(a) > 0:
        overflow = 0
        dec_a = int(a.pop(), 16) if len(a) > 0 else 0
        b2 = b.copy()
        c2 = deque(level)
        while len(b2) > 0:
            dec_b = int(b2.pop(), 16) if len(b2) > 0 else 0
            n = dec_a * dec_b + overflow
            c2.appendleft(hex_base[n % len(hex_base)])
            overflow = n // len(hex_base)
        if overflow > 0:
            c2.appendleft(hex_base[overflow])
        c.appendleft(c2)
        level += '0'
    return reduce(sum_hex, c)


print("\nС применением deque")
a_dq = deque(a_hex)
b_dq = deque(b_hex)
print(a_dq)
print(b_dq)

c_dq = sum_hex(a_dq, b_dq)
print(c_dq)

d_dq = mul_hex(a_dq, b_dq)
print(d_dq)


########################################
def named(n):
    """Создание порядкового имени для словаря"""
    sn = 'abcdefghijklmnopqrstuvwxyz'
    name = deque()
    while n >= 0:
        name.appendleft(sn[n % len(sn)])
        n = n // len(sn) - 1
    return ''.join(name)


def counter_to_hex(c_cnt):
    """
    Функция переводит суммы счетчика в очередь из шестнадцатиричных чисел

    :param c_cnt: Счетчик с суммами по разрядам
    :return: Возвращает очередь с шестнадцетиричными числами
    """
    s = deque()
    overflow = 0
    for i in range(len(c_cnt)):
        key = named(i)
        s.appendleft(hex_base[c_cnt[key] % len(hex_base) + overflow])
        overflow = c_cnt[key] // len(hex_base)
    if overflow > 0:
        s.appendleft(hex_base[overflow])
    return s


def sum_hex_by_counter(source_a, source_b):
    """
    Функци суммирования двух шестнадцатиричных чисел, представленных в виде очередей

    :param source_a: Число a
    :param source_b: Число b
    :return: Возвращает сумму в виде ряда шестнадцетиричных чисел
    """
    a_cnt = Counter({named(len(source_a) - i - 1): int(n, 16) for i, n in enumerate(source_a)})
    b_cnt = Counter({named(len(source_b) - i - 1): int(n, 16) for i, n in enumerate(source_b)})
    c_cnt = a_cnt + b_cnt
    return counter_to_hex(c_cnt)


def mul_hex_by_counter(source_a, source_b):
    """
    Функци произведения двух шестнадцатиричных чисел, представленных в виде очередей

    :param source_a: Число a
    :param source_b: Число b
    :return: Возвращает произведение в виде ряда шестнадцетиричных чисел
    """
    c_cnt = Counter()
    a = source_a.copy()
    i = 0
    while len(a) > 0:
        j = 0
        num_a = int(a.pop(), 16)
        b = source_b.copy()
        while len(b) > 0:
            c_cnt[named(i + j)] += int(b.pop(), 16) * num_a
            j += 1
        i += 1
    return counter_to_hex(c_cnt)


print("\nС применеием Counter и deque")
c_3 = sum_hex_by_counter(a_dq, b_dq)
print(c_3)

d_3 = mul_hex_by_counter(a_dq, b_dq)
print(d_3)

