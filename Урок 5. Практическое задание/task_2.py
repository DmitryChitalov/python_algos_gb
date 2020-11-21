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

class MathOperationHex:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]

print('Program "Addition and multiplication of two hexadecimal numbers"')
first_hex_number = list(input('Please enter first hex number: '))
second_hex_number = list(input('Please enter second hex number: '))

result_sum = MathOperationHex(first_hex_number, second_hex_number) + MathOperationHex(first_hex_number, second_hex_number)
result_multi = MathOperationHex(first_hex_number, second_hex_number) * MathOperationHex(first_hex_number, second_hex_number)

print(f'Sum of {first_hex_number} and {second_hex_number} is: {result_sum}')
print(f'Multiplication of {first_hex_number} and {second_hex_number} is: {result_multi}')