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
import collections as coll

num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))
dict1 = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}
res = coll.deque()
counter = 0
num = 0


#Переводим числа в шестнадцатеричные
def convert(num):
    if num > 15:
        remain = num % 16
        if remain < 10:
            res.appendleft(remain)
        elif remain in dict1:
            res.appendleft(dict1[remain])
        num = num // 16
        convert(num)
    else:
        if num < 10:
            res.appendleft(num)
        elif num in dict1:
            res.appendleft(dict1[num])
        return


def sum(num_1, num_2):
    summ = num_1 + num_2
    convert(summ)
    return


def mul(num_1, num_2):
    mult = num_1 * num_2
    convert(mult)
    return


sum(num1, num2)
print(res)
res.clear()
mul(num1, num2)
print(res)
res.clear()

'''
Резюме: не понял, как применить коллекцию при введении шестнадцатеричного числа,
поэтому добавил конвертер 10 -> 16
'''