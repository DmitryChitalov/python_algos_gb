"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random

rand_num = random.randint(0, 100)
print('Введите числа от 0 до 100')


def random_value(**data):
    try:
        data_rand = data['rand_num']
        data_value = data['value']
        data_mass = data['mass']
        if len(data_mass) == 10:
            return f'Вы не отгадали число {data_rand}'
        else:
            if data_value != data_rand:
                data_mass.append(data_value)
                if data_value > data_rand:
                    print('Число больше рандомного')
                else:
                    print('Число меньше рандомного')
                data_value = int(input('Value: '))
                return random_value(rand_num=data_rand, value=data_value, mass=data_mass)
            else:
                return f'Обалдеть вы угадали число {data_rand} с попытки номер {len(data_mass) + 1}'
    except ValueError:
        print('Only int!')
try:
    user_inp = int(input('Value: '))
    print(random_value(rand_num=rand_num, value=user_inp, mass=[]))
except ValueError:
    print('Only int! Try again!')
    user_inp = int(input('Value: '))
    print(random_value(rand_num=rand_num, value=user_inp, mass=[]))