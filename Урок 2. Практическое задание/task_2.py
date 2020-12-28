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

# def estimation(number, even = 0, odd = 0):
#     if len(number) == 1:
#         return even, odd
#     else:
#         digit = int(number[0])%2
#         if digit == 0:
#             even += 1
#         else:
#             odd += 1
#         estimation(number[1:])

# print(estimation('12348'))
# Делить на 10 и брать остаток - так уменьшать число
# def est(number, even=0, odd=0):
#     while number != 0:
#         number = int(number)
#         digit = number % 2
#         number = number//10
#         if digit == 0:
#             even += 1
#         else:
#             odd += 1
#     print(even)
#     print(odd)
#
#
# est('123456789')

def estimation(number, even=0, odd=0):
    number = int(number)
    if number == 0:
        return even, odd
    else:
        digit = number % 10
        number = number//10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        return estimation(number, even, odd)

print(estimation(224466))