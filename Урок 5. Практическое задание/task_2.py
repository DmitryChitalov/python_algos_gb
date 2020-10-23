"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
from functools import reduce

a = 'A2'
b = 'C4F'
def calc():
    nums = defaultdict(list)
    for digit in range(2):
        number = input('Введите шестнадцатиричное число')
        nums[number] = list(number)
        print(nums)

    sum_nums = sum([int(''.join(i), 16) for i in nums.values()])
    print(f'Сумма: {hex(sum_nums)[2:].upper()}')
    mult_nums = reduce(lambda a,b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print(f'Произведение: {hex(mult_nums).upper()}')

calc()

'''
a_lst = list(''.join(a))
b_lst = list(''.join(b))
print(a_lst, b_lst)
a_10 = int(a, 16)
b_10 = int(b, 16)
print(a_10, b_10)
sum_ab = a_10 + b_10
prod_ab = a_10 * b_10
print(hex(sum_ab)[2:].upper())
print(hex(prod_ab)[2:])
'''
