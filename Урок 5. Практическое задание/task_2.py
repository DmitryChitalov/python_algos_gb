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
from collections import deque


def rec_hex_to_dec(number, n=0):
    n = len(number)-1
    if n == -1:
        return 0
    else:
        k = '0123456789ABCDEF'.index(number.popleft())
        return k * (16**n) + rec_hex_to_dec(number, n-1)


def rec_dec_to_hec(number, result=''):
    if result == '':
        result = deque(list(result))
    if number < 16:
        return result.appendleft('0123456789ABCDEF'[number])
    else:
        result.appendleft('0123456789ABCDEF'[(number - (16 * (number // 16)))])
        return result, rec_dec_to_hec(number // 16, result)


deq_num_1 = deque(list(input('Введите первое число: ')))
print(f'Число 1 хранится в виде массива: {list(deq_num_1)} ')
deq_num_2 = deque(list(input('Введите первое число: ')))
print(f'Число 2 хранится в виде массива: {list(deq_num_2)} ')

dec_num_1 = rec_hex_to_dec(deq_num_1.copy())
dec_num_2 = rec_hex_to_dec(deq_num_2.copy())
print(f'Сумма чисел = {list(rec_dec_to_hec(dec_num_1+dec_num_2)[0])}, '
      f'произведение = {list(rec_dec_to_hec(dec_num_1*dec_num_2)[0])}')
