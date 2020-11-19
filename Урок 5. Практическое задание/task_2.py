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


# вариант с деком, с переворотом вводимых данных по ходу выполнения программы, по сути просто так
def variant_1():
    input_list, output_list = deque(), deque()

    def check_symbol(data):
        while True:
            for i in data:
                if i.lower() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f'):
                    print('Ошибка ввода.')
                    data = input('Пожалуйста, введите шестнадцатеричное число: ')
                    break
            return data

    for i in range(2):
        input_list.append(deque())
        output_list.append(deque())
        user_input = check_symbol(input(f'Введите число {i + 1}: '))
        for j in user_input:
            input_list[i].append(j)

    nums_list = deque()

    for i in range(len(input_list) - 1, -1, -1):
        nums = ''
        for j in input_list[i]:
            nums += j
        nums_list.appendleft(nums)

    nums_summ = hex(int(nums_list[0], 16) + int(nums_list[1], 16)).split('x')[-1]
    nums_mult = hex(int(nums_list[0], 16) * int(nums_list[1], 16)).split('x')[-1]

    for i in nums_summ:
        output_list[0].append(i)

    for i in nums_mult:
        output_list[1].append(i)

    for n in range(len(output_list)):
        if n == 0:
            print('Сумма введённых чисел: ')
        else:
            print('Произведение введённых чисел: ')
        for d in output_list[n]:
            print(str(d).upper(), end='')
        print()


# вариант на ООП:
def variant_2():
    class MyDigit:
        def __init__(self, num):
            self.num = int(num, 16)

        def __add__(self, other):
            return hex(self.num + other.num).split('x')[-1].upper()

        def __mul__(self, other):
            return hex(self.num * other.num).split('x')[-1].upper()

    aa = MyDigit('a2')
    bb = MyDigit('c4f')
    print(aa + bb)
    print(aa * bb)

# variant_1()
# variant_2()
