"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# проверка ввода на число:
def is_a_digit(data):
    while not data.isdigit():
        print(f'Ошибка ввода. Пожалуйста, введите одно целое натуральное число.\n')
        data = input('Введите число: ')
    return data


# только вычисление уравнения с подстановкой путём рекурсии:
def rec(n='', num=0):
    if isinstance(n, str):
        n = int(n)
    if int(n) > 0:
        return rec(n - 1, num + n)
    else:
        return f'Посчитано: {num}'


# print(rec(is_a_digit(input('Введите целое натуральное число: '))))

# решение с проверкой:
def rec_2(n='', str_out='', num=0):
    global user_input
    if isinstance(user_input, str):
        user_input = int(user_input)
    if isinstance(n, str):
        n = int(n)
    if int(n) > 0:
        return rec_2(n - 1, str_out + str(n)[::-1] + '+', num + n)
    else:
        if num == (user_input * (user_input + 1)) / 2:
            print(f'Программой посчитано:\n'
                  f'{str_out[::-1].lstrip("+")} = {num},\n{user_input}*({user_input}+1)/2 = {num},\nследовательно:\n'
                  f'{str_out[::-1].lstrip("+")} = {user_input}*({user_input}+1)/2.')
            return
        else:
            return 'Error'


user_input = is_a_digit(input('Введите целое натуральное число: '))
rec_2(user_input)
