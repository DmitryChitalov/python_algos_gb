"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def get_even_digits_info_recursive(initial_value: int, current_number: int = None, current_even_digits_count: int = 0,
                                   current_not_even_digits_count: int = 0):
    if initial_value == 0:
        return 1, 0
    elif current_number == 0:
        return current_even_digits_count, current_not_even_digits_count
    else:
        if current_number is None:
            current_number = initial_value
        current_digit = current_number % 10
        number_without_current_digit = current_number // 10
        if current_digit % 2 == 0:
            current_even_digits_count += 1
        else:
            current_not_even_digits_count += 1
        return get_even_digits_info_recursive(initial_value, number_without_current_digit, current_even_digits_count,
                                              current_not_even_digits_count)


try:
    number = int(input("Введите натуральное число: "))
    even_digits_info = get_even_digits_info_recursive(number)
    print(f"Количество четных цифр в числе '{number}': {even_digits_info[0]}, нечётных: {even_digits_info[1]}.")
except ValueError:
    print("Число не является целым.")
