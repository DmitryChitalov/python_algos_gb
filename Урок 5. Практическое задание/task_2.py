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

num1 = list(input('Введите первое число: ').upper())
num2 = list(input('Введите второе число: ').upper())


class HexDigits:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        result = hex(int(''.join(self.num1), 16) + int(''.join(other.num2), 16))
        return list(result)[2:]

    def __mul__(self, other):
        result = hex(int(''.join(self.num1), 16) * int(''.join(other.num2), 16))
        return list(result)[2:]


print(f'Вы ввели {num1} и {num2}')
sum = HexDigits(num1, num2) + HexDigits(num1, num2)
sum = [x.upper() for x in sum]
mul = HexDigits(num1, num2) * HexDigits(num1, num2)
mul = [x.upper() for x in mul]
print(f'Сумма чисел = {sum}')
print(f'Произведение чисел = {mul}')
