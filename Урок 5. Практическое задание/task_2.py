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

# -= variables section =-
import functools

next_inter = True
defdict = collections.defaultdict(list)


def defdict_init(a, b):
    defdict[1] = list(a)
    defdict[2] = list(b)
    print(defdict)


def summ():
    v_result = sum([int(''.join(i), 16) for i in defdict.values()])
    print(f'[INFO]: Сумма чисел "{defdict[1]}" и "{defdict[2]}" = {"0x%0.2X" % v_result} ({v_result})')
    return v_result


def multic():
    v_result = functools.reduce(lambda _a, _b: _a * _b, [int(''.join(i), 16) for i in defdict.values()])
    print(f'[INFO]: Произведение чисел "{defdict[1]}" и "{defdict[2]}" = {"0x%0.2X" % v_result} ({v_result})')
    return v_result


if __name__ == "__main__":
    while next_inter:
        number_a = input("Введите число A : ")
        number_b = input("Введите число B : ")

        defdict_init(number_a, number_b)
        summ()
        multic()

        while True:
            next_add = input("Хотите выполнить дополнительный расчет? (Да / Нет): ")
            if next_add.lower() in ('да', 'нет', 'yes', 'no', 'y', 'n'):
                next_inter = next_add.lower() in ('да', 'yes', 'y')
                break
            else:
                print("Ошибка ввода: введите ответ еще раз")

    print("- " * 50)
