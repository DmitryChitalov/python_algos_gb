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
import collections

def sum_hexadecimal(input_dict):
    num1 = int(''.join(input_dict['num1']), base =16)
    num2 = int(''.join(input_dict['num2']), base = 16)
    num_sum = num1 + num2
    return hex(num_sum)


def mult_hexadecimal(input_dict):
    num1 = int(''.join(input_dict['num1']), base =16)
    num2 = int(''.join(input_dict['num2']), base = 16)
    num_mult = num1 * num2
    return hex(num_mult)

input_num1 = 'A2'
input_num2 = 'C4F'

num_list1 = [i for i in input_num1]
num_list2 = [i for i in input_num2]
print(f'введено число 1: {num_list1}')
print(f'введено число 2: {num_list2}')

numbs_dict = collections.defaultdict(list, [('num1', num_list1),('num2', num_list2)])
print(numbs_dict)
print()

sum_result = sum_hexadecimal(numbs_dict)
print(f'результат сложения: {sum_result}')

mult_result = mult_hexadecimal(numbs_dict)
print(f'результат умножения: {mult_result}')