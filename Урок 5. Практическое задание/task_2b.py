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


class Number:
    def __init__(self, number):
        self.number = ''.join(number)

    def __add__(self, other):
        return (hex(int(float.fromhex(self.number)) + int(float.fromhex(other.number))))[2:].upper()

    def __mul__(self, other):
        return (hex(int(float.fromhex(self.number)) * int(float.fromhex(other.number))))[2:].upper()


first_num = list(input('Введите первое число '))
second_num = list(input('Введите второе число '))

sum_16 = Number(first_num) + Number(second_num)
mult_16 = Number(first_num) * Number(second_num)
print(f'Сумма введенных чисел - {sum_16}')
print(f'Произведение введенных чисел - {mult_16}')
