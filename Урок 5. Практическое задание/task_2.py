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


class HexadecimalNumber:
    def __init__(self, input_hex):
        self.input_number = int(input_hex, 16)

    def __str__(self):
       return str(hex(self.input_number).split('0x')[1].upper())

    def __add__(self, other):
       return HexadecimalNumber(hex(self.input_number + other.input_number))

    def __mul__(self, other):
        return HexadecimalNumber(hex(self.input_number * other.input_number))


if __name__ == '__main__':
    a = HexadecimalNumber('A2')
    b = HexadecimalNumber('C4F')
    print(a, b)
    c = a + b
    d = a * b
    print(c, d)

    one = 'A2'
    two = 'C4F'
    if one < two:
        one, two = two, one

    a = collections.deque(one)
    b = collections.deque(two)
    c = collections.deque()

    more_than_fifteen = 0
    for i in range(len(a)):
            try:
                num = int(a.pop(), 16)
                num += int(b.pop(), 16)
                num += more_than_fifteen
            except IndexError:
                pass
            if num > 15:
                more_than_fifteen = 1
                num = num - 16
            else:
                more_than_fifteen = 0

            c.appendleft(hex(num).split('0x')[1].upper())

    print(c)
    a = collections.deque(one)
    b = collections.deque(two)

    three = hex(int(one, 16) * int(two, 16)).split('0x')[1].upper()
    d = collections.deque(three)

    print(d)


