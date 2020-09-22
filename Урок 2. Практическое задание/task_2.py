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


def number_of_even_and_odd_digits_in_user_number(user_number, idx_odd = [], idx_even = []):
    user_list = list(str(user_number))
    if len(user_list) == 1:
        if int(user_list[0]) % 2 == 0:
            idx_even.append(int(user_list[0]))
        elif int(user_list[0]) % 2 != 0:
            idx_odd.append(int(user_list[0]))
        print(f'Количество чётных цифр: {len(idx_even)}, НЕчётных: {len(idx_odd)}')
        return True
    else:
        number = int(user_list.pop())
        if number%2 == 0:
            idx_even.append(number)
        elif number%2 != 0:
            idx_odd.append(number)
        next_number = int(''.join(user_list))
        number_of_even_and_odd_digits_in_user_number(next_number)


number_of_even_and_odd_digits_in_user_number(user_number = int(input('Введите число: ')))