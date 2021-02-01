"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля
collections
Для лучшее освоения материала можете даже сделать несколько решений этого
задания, применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши
знания по ООП (в частности по перегрузке методов)
"""


class MyHex:
    check_string = '0123456789ABCDEF'

    def __init__(self, hex_number):
        self.check_numbers(hex_number, self.check_string)
        self._hex_number = hex_number

    def __str__(self):
        return self._hex_number

    def __add__(self, other):
        if isinstance(other, MyHex):
            result_sum = int(self._hex_number, 16) + int(other._hex_number, 16)
            result_sum_str = str(hex(result_sum))[2:].upper()
            return MyHex(result_sum_str)
        raise TypeError(f'unsupported operand type(s) '
                        f'+: "{type(self)}" and "{type(other)}"')

    def __mul__(self, other):
        if isinstance(other, MyHex):
            result_mul = int(self._hex_number, 16) * int(other._hex_number, 16)
            result_mul_str = str(hex(result_mul))[2:].upper()
            return MyHex(result_mul_str)
        raise TypeError(f'unsupported operation'
                        f' *: "{type(self)}" and "{type(other)}"')

    @staticmethod
    def check_numbers(hex_number, check_string):
        if isinstance(hex_number, str):
            for n in hex_number:
                if n.upper() in check_string:
                    return hex_number
        raise ValueError('Incorrect hex number')


if __name__ == '__main__':
    a = MyHex('A2')
    print(a)
    b = MyHex('C4F')
    print(b)
    c = a + b
    print(c)
    d = a * b
    print(d)
