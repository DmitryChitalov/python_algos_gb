"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def check_left(var_int):
    if var_int == 1:
        return 1
    return var_int + check_left(var_int - 1)


var_str = input("Введите число > 0 : ")
while not var_str.isdigit():
    print("Введено не число")
    var_str = int("Введите число > 0: ")
var_int = int(var_str)

var_left = check_left(var_int)
var_right = var_int * (var_int + 1) / 2

if var_left == var_right:
    print(f"1+2+...+n = n(n+1)/2")
    print(f"{var_left} = {var_right}")
else:
    print(f"1+2+...+n != n(n+1)/2")
    print(f"{var_left} != {var_right}")
