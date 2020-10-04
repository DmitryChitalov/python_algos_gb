"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
#n = 20
#e = 1
def summa(a, num):
    if (num == 0):
        return 0
    else:
        return a[num - 1] + summa(a, num-1)
e = 1
s = []
n = int(input('Введите количество чисел ряда: '))
for i in range(n):
    s.append(e)
    e /= -2
print(s)
print(f'Сумма: {summa(s, n)}')





#def summa(r):
#    n =
#    if n == 0:
#        return 0
#   else:
#        return r[n - 1] + summa(r)

#print(f'{summa()}')





#print(f'{summa(1)}')


#def sum():
#    n = int(input())
#    if n != 0:
#        return n + sum()
#    return 0


#print(sum())