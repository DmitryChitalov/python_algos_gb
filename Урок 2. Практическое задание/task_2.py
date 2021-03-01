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


def even_odd(number: int, a, b):
    next_number = number // 10
    if (number % 10) % 2 == 0:
        a += 1
    else:
        b += 1

    if next_number == 0:
        return a, b

    return even_odd(next_number, a, b)


try:
    num = int(input("Введите число: "))
except ValueError:
    print("Некорректный ввод ")

print(f"Количество четных и нечетных цифр в числе равно: {even_odd(num, 0, 0)}")
