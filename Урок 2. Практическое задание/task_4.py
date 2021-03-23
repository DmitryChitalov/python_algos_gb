"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

MAXN = 100


# вычисление суммы непосредственно
def serial_sum(n, x=1, s=0):
    if n == 0:
        return s
    return serial_sum(n-1, -0.5*x, x+s)


# и по формуле суммы геометрической прогрессии
def exact_sum(n):
    return (1 - (-0.5)**n)/1.5


while True:
    try:
        n = int(input(f"Введите число от 1 до {MAXN}: "))
    except ValueError:
        continue
    if n >= 1 and n <= MAXN:
        break

print(f"Считаем сумму {n} членов геометрической прогрессии")
print("Непосредственно: ", serial_sum(n))
print("По формуле: ", exact_sum(n))
