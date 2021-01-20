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
def parity(number, even  = 0, odd = 0):
    number = str(number)
    even = even
    odd = odd
    c = int(number[0])
    if c % 2 == 0:
        even += 1
    else:
        odd += 1
    if len(number) == 1:
        return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
    else:
        return parity(number[1:], even, odd)

print(parity(12345))