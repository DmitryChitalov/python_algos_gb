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




import functools
import collections
def sixteen():
    numbers = collections.defaultdict(list)
    for i in range(2):
        user_number = input(f'Введите {i+1} натуральное шестнадцатиричное число: ')
        numbers[f'{i+1}--{user_number}'] = list(user_number)
        print(numbers)

        summ = sum([int(''.join(j), 16) for j in numbers.values()])

        print(f'Итоговая сумма: {list("%x" % summ)}')

        multiply = functools.reduce(lambda a,b: a * b, [int("".join(j), 16) for j in numbers.values()])
        print(f'Произведение: {list("%X" % multiply)}')


sixteen()