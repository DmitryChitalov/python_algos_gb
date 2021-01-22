"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def count_numbers(number, even_numbers = 0, odd_numbers = 0):
    if number == 0:
        return even_numbers, odd_numbers

    else:
        check_digit = number % 10

        number = number // 10

        if check_digit % 2 == 0:
            even_numbers += 1
            return count_numbers(number, even_numbers, odd_numbers)

        else:
            odd_numbers += 1
            return count_numbers(number, even_numbers, odd_numbers)

try:
    number_to_be_checked = int(input('Введите число: '))
    print(f'Количество четных и нечетных цифр в числе равно: {count_numbers(number_to_be_checked)}')
except ValueError:
    print('Введите число')





