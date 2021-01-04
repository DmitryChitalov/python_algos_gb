"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

c Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
  (в частности по перегрузке методов)
"""

"""
nums1 = input('Введите шестнадцатеричное число'
              '(шестнадцатеричное число состоит из цифр от 0 до 9 и букв A, B, C, D, E, F):\n').upper()
nums2 = input('Введите второе шестнадцатеричное число'
              '(шестнадцатеричное число состоит из цифр от 0 до 9 и букв A, B, C, D, E, F):\n').upper()

hex_nums1 = int('0x' + nums1, 16)
hex_nums2 = int('0x' + nums2, 16)
sum_hex = list(hex(hex_nums1 + hex_nums2).upper()[2:])
print(sum_hex)
m_hex = list(hex(hex_nums1 * hex_nums2).upper()[2:])
print(m_hex)
"""


class Hexadecimal:
    def __init__(self, nums):
        self.nums = int('0x' + str(nums).upper(), 16)

    def __add__(self, other):
        summ_hex = self.nums + other.nums
        return list(hex(summ_hex).upper()[2:])

    def __mul__(self, other):
        m_hex = self.nums * other.nums
        return list(hex(m_hex).upper()[2:])

    def __str__(self):
        return f'{list(hex(self.nums).upper()[2:])}'


hex_number1 = Hexadecimal('a2')
hex_number2 = Hexadecimal('c4f')
print(f'Первое шестнадцатеричное число: {hex_number1}')
print(f'Второе шестнадцатеричное число: {hex_number2}')
print(f'Сумма шестнадцатеричных чисел: {hex_number1 + hex_number2}')
print(f'Произведение шестнадцатеричных чисел: {hex_number1 * hex_number2}')
