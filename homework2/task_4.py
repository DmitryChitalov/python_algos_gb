"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

Элемент в 2 раза меньше предыд и имеет противопол знак
"""
n = int(input('Введите количество элементов: '))
def count_n(n, number=1, summ=1, count=1):
    if n == 1:
        return 1
    if count % 2 != 0:
        number = -(number / 2)
    else:
        number = abs(number / 2)
    summ += number
    if count == n-1:
        return summ
    count += 1
    return count_n(n, number, summ, count)

print(count_n(n))