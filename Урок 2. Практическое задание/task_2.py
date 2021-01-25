"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def numbers(**data):
    try:
        data_list = data['user_inp']
        data_even = data['even']
        data_odd = data['odd']
        if len(data_list) == 1:
            if int(data_list[0]) % 2 == 0:
                data_even += 1
                return data_even, data_odd
            else:
                data_odd += 1
                return data_even, data_odd
        else:
            if int(data_list[0]) % 2 == 0:
                data_even += 1
                return numbers(user_inp=data_list[1:], even=data_even, odd=data_odd)
            else:
                data_odd += 1
                return numbers(user_inp=data_list[1:], even=data_even, odd=data_odd)
    except ValueError:
        print('str value! Pls try again')
        return numbers(user_inp=list(input('Your value:')), even=0, odd=0)


user_inp = list(input('Your value:'))
print(f'Количество четных и нечетных цифр в числе равно: {numbers(user_inp=user_inp, even=0, odd=0)}')

