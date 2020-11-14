"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import sys


def input_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit():
        print("Недопустимый ввод!")
        res = input_number(message)

    return int(res)


def print_proof(res_left, res_right):
    if res_left != 0 and res_right != 0:
        if res_left == res_right:
            print(f"left ({res_left}) равно right({res_right})")
        else:
            print(f"left ({res_left}) не равно right({res_right})")


def do_proove(user_number):
    pass

    res_left = 0
    res_right = 0

    if user_number == 0:
        return 0, 0

    left = user_number
    right = user_number * (user_number + 1) / 2

    # print(f"left({left}) | right({right})")
    user_number -= 1
    tleft, tright = do_proove(user_number)

    res_left += tleft
    res_right += tright

    print_proof(res_left, res_right)

    return left, right


def main():
    pass
    # try:
    sys.setrecursionlimit(100000)
    user_number = input_number("Введите число: ")

    res_left, res_right = do_proove(user_number)
    # печатаем последнее число из диапазона, т.к. функция возвращала значение
    print_proof(res_left, res_right)

    print("Программа завершена!")
    # except Exception as ex:
    #     print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
