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
from collections import namedtuple
from functools import reduce

# Решение 1 через collections
template_num = namedtuple('num', 'one_num two_num')
num_hex = template_num(
    one_num=' '.join(input('Введите первое 16-ричное число: ')).upper().split(),
    two_num=' '.join(input('Введите второе 16-ричное число: ')).upper().split()
)
num_int = template_num(
    one_num=int(reduce(lambda x, y: x + y, num_hex.one_num), 16),
    two_num=int(reduce(lambda x, y: x + y, num_hex.two_num), 16)
)
sum_num = num_int.one_num + num_int.two_num
prod_num = num_int.one_num * num_int.two_num
sum_num_hex = ' '.join(str(hex(sum_num))[2:].upper()).split()
prod_num_hex = ' '.join(str(hex(prod_num))[2:].upper()).split()
print(f'Решение через collections')
print(f'Первое число {num_hex.one_num}')
print(f'Второе число {num_hex.two_num}')
print(f'Сумма чисел {sum_num_hex}')
print(f'Произведение чисел {prod_num_hex}')

# Решение 2 через ООП


class HexNumber:
    def __init__(self, num):
        self.num = ' '.join(num).upper().split()

    def __add__(self, other):
        return HexNumber(' '.join(str(hex(int(reduce(lambda x, y: x + y, self.num), 16) +
                         int(reduce(lambda x, y: x + y, other.num), 16)))[2:].upper().split()))

    def __mul__(self, other):
        return HexNumber(' '.join(str(hex(int(reduce(lambda x, y: x + y, self.num), 16) *
                                          int(reduce(lambda x, y: x + y, other.num), 16)))[2:].upper().split()))

    def __str__(self):
        return f'{" ".join(self.num).upper().split()}'


print()
print('Решение через ООП')
num_one = HexNumber(num_hex.one_num)
num_two = HexNumber(num_hex.two_num)
s_num = num_one + num_two
p_num = num_one * num_two
print(f'Первое число {num_one.num}')
print(f'Второе число {num_two.num}')
print(f'Сумма чисел {s_num}')
print(f'Произведение чисел {p_num}')

'''
Возможно в ООП не так сделал, но по сути просто реализовал все так же как и не через ООП
Не понял как реализовать через defaultdict, пробовал, эксперементировал, но все равно получается не очень, поэтому
сделал через namedtuple
'''

