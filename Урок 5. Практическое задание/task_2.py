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

class HexNumb:
    def __init__(self, str_number):
        self.str_number = str_number
        # Сохраняем как массив.
        self.number = deque([symb.upper() for symb in str_number])
        self._translate_dict = defaultdict(int, {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15})
        self._translate_redict = defaultdict(int, {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"})

    @staticmethod
    def go_int_power(numb, degree):
        result = 1
        for _ in range(degree):
            result *= numb
        return result

    def _to_number(self, user_str):
        """Переводит в число."""
        result_int = self._translate_dict[user_str]
        return result_int or int(user_str)

    def _to_int(self, user_deque):
        """Переводит в десятичное."""
        tmp_deque = user_deque.copy()
        result_int = 0
        tmp_deque.reverse()
        for numb, symb in enumerate(tmp_deque):
            result_int += self._to_number(symb) * self.go_int_power(16, numb)
        return result_int

    def _to_hex(self, user_int):
        """Переводит в шестнадцатиричное."""
        result_hex = deque()
        while user_int:
            _to_hex_value = user_int - user_int // 16 * 16
            user_int //= 16
            append_value = self._translate_redict[_to_hex_value % 16] if self._translate_redict[_to_hex_value % 16] else str(_to_hex_value % 16)
            result_hex.append(append_value)
        result_hex.reverse()
        return ''.join(result_hex)

    def __str__(self):
        return self.str_number

    def __add__(self, other):
        """Сложение."""
        result_int = self._to_int(self.number) + self._to_int(other.number)
        result_hex = self._to_hex(result_int)
        return HexNumb(result_hex)

    def __mul__(self, other):
        """Произведение."""
        result_int = self._to_int(self.number) * self._to_int(other.number)
        result_hex = self._to_hex(result_int)
        return HexNumb(result_hex)

numb_1 = HexNumb('A2')
numb_2 = HexNumb('C4F')
numb_3 = HexNumb('D9')

numb_4 = numb_1 + numb_2
numb_5 = numb_1 + numb_2 + numb_3
numb_6 = numb_1 * numb_2
numb_7 = numb_1 * numb_2 * numb_3

print(f'Сложение:\t{numb_1} + {numb_2} = {numb_4}\t\t[{type(numb_4)}]')
print(f'Сложение:\t{numb_1} + {numb_2} + {numb_3} = {numb_5}\t[{type(numb_5)}]')
print(f'Умножение:\t{numb_1} * {numb_2} = {numb_6}\t[{type(numb_6)}]')
print(f'Умножение:\t{numb_1} * {numb_2} * {numb_3} = {numb_7}\t[{type(numb_7)}]')

"""
Результат выполнения программы.
    Сложение:       A2 + C4F = CF1          [<class '__main__.HexNumb'>]
    Сложение:       A2 + C4F + D9 = DCA     [<class '__main__.HexNumb'>]
    Умножение:      A2 * C4F = 7C9FE        [<class '__main__.HexNumb'>]
    Умножение:      A2 * C4F * D9 = 69A384E [<class '__main__.HexNumb'>]
"""
