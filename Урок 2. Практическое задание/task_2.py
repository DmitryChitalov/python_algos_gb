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


def rec_even(user_input, even, odd):
    if user_input == 0:  # условие завершения
        return even, odd
    else:  # иначе делаем и опять запускаем
        extract_num = user_input % 10
        user_input //= 10

        if extract_num % 2 != 0:
            odd += 1
            return rec_even(user_input, even, odd)
        else:
            even += 1
            return rec_even(user_input, even, odd)


u_input = input('Enter a number: \n')
if u_input.isnumeric():
    print(f'Even - {rec_even(int(u_input), 0, 0)[0]}, '
          f'odd - {rec_even(int(u_input), 0, 0)[1]}')
else:
    print('You must enter a number')
