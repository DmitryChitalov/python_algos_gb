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


class Hexadecimal:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]


hex_first_num = list(input('Введите первое шестанадцатеричное число: '))
hex_second_num = list(input('Введите второе шестнадцатеричное число: '))

sum_result = Hexadecimal(hex_first_num, hex_second_num) + Hexadecimal(hex_first_num, hex_second_num)
mul_result = Hexadecimal(hex_first_num, hex_second_num) * Hexadecimal(hex_first_num, hex_second_num)

print(f'Сумма чисел: {sum_result}\nПроизведение чисел: {mul_result}')
