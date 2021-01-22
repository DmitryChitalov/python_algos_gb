"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def number_sum(**data):
    try:
        data_mass = data['mass']
        if len(data['mass']) == data['limit']:
            return f'Количество элементов - {data["limit"]}, их сумма - {sum(data_mass)}'
        else:
            user_values = float(input('values: '))
            data_mass.append(user_values)
            return number_sum(limit=user_inp, mass=data_mass)

    except ValueError:
        print('Error')


user_inp = int(input('Введите желаемое количество элементов: '))
print(number_sum(limit=user_inp, mass=[]))