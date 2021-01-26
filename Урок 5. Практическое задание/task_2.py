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
from collections import deque, defaultdict


class Arp16:
    def __init__(self, num):
        self.dic_def = defaultdict(int)
        cnt = 0
        for el in '0123456789ABCDEF':
            self.dic_def[el] += cnt
            cnt += 1
        self.num = self.convert_to_dec(num)

    def convert_to_dec(self, string):
        dex = 0
        num = deque(string)
        num.reverse()
        for i in range(len(num)):
            dex += self.dic_def[num[i]] * 16 ** i
        return dex

    def convert_to_hex(self, numb):
        num = deque()
        while numb > 0:
            d = numb % 16
            for i in self.dic_def:
                if self.dic_def[i] == d:
                    num.append(i)
            numb //= 16
        num.reverse()
        return list(num)

    def __add__(self, other):
        return Arp16(self.convert_to_hex(self.num + other.num))

    def __mul__(self, other):
        return Arp16(self.convert_to_hex(self.num * other.num))

    def __str__(self):
        return str(self.convert_to_hex(self.num))


num_1 = Arp16(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = Arp16(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {num_1 + num_2}')
print(f'Произведение чисел: {num_1 * num_2}')