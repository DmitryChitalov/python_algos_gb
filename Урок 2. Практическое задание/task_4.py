"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

# def calculation():
#     n = int(input('Введите число n:  '))
#     start_number = int(input('Введите стартовое число:'))
#     step = int(input('Введите шаг деления:  '))
#     numbers = []
#     for i in range(1, n+1):
#         calc = start_number
#         numbers.append(calc)
#         print(calc)
#         start_number = start_number*-1/step
#     summa = sum(numbers)
#     return summa
#
# print(calculation())


n = int(input('Введит число циклов n:  '))
def calculation(n, number = 1, numbers=[1]):
    if n == 1:
        return numbers, sum(numbers)
    else:
        number = (number * -1)/2
        n -= 1
        numbers.append(number)
        return calculation(n, number, numbers)


print(calculation(n))