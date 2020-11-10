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


def count_evens(number, cycle_count):
    pass
    even_count = 0
    neven_count = 0
    cycle_count -= 1
    if cycle_count < 0:
        return even_count, neven_count

    print(f"postion: {cycle_count +1}: num in position {number[cycle_count]}")
    if int(number[cycle_count]) % 2 == 0:
        even_count += 1
    else:
        neven_count += 1
    res_even, res_neven = count_evens(number, cycle_count)
    even_count += res_even
    neven_count += res_neven
    return even_count, neven_count


def input_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit():
        print("Недопустимый ввод!")
        res = input_number()

    return res


def main():
    pass
    try:
        number = input_number("Введите число: ")
        even_count, neven_count = count_evens(number, len(number))
        print(f"В числе {number}: четных чисел {even_count};  не четных чисел {neven_count}")
        print("Программа завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
