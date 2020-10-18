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

def set_16(num1: str, num2: str):
    from collections import defaultdict

    for char in num1 + num2:
        if not char in '0123456789abcdef':
            print('Некорректный ввод.')
            return
    nums = defaultdict(list)
    for char in num1:
        nums[1].append(char)
    for char in num2:
        nums[2].append(char)
    return nums

def addition_16(nums):
    from functools import reduce

    if nums:
        res = 0
        for num in nums.values():
            res += int(reduce(lambda x, y: x + y, num), 16)
        return hex(res)

def multiplication_16(nums):
    from functools import reduce

    if nums:
        res = 1
        for num in nums.values():
            res *= int(reduce(lambda x, y: x + y, num), 16)
        return hex(res)

class HexNum():
    def __init__(self, num):
        for char in str(num):
            if not char in '0123456789abcdef':
                print('Некорректный ввод.')
                return
        self.num = num

    def __add__(self, other):
        try:
            return hex(int(self.num, 16) + int(other.num, 16))
        except AttributeError:
            print('Некорректные аргументы.')

    def __mul__(self, other):
        try:
            return hex(int(self.num, 16) * int(other.num, 16))
        except AttributeError:
            print('Некорректные аргументы.')

if __name__ == '__main__':
    nums = set_16(input('Введите первое число: '),
                  input('Введите второе число: '))
    print(f'Результат сложения: {addition_16(nums)}')
    print(f'Результат умножения: {multiplication_16(nums)}')

    num1 = HexNum(input('Введите первое число: '))
    num2 = HexNum(input('Введите второе число: '))
    print(f'Результат сложения: {num1 + num2}')
    print(f'Результат умножения: {num1 * num2}')