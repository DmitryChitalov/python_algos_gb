"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
'''#n=int(input('Введите количество элементов:'))
lst=[]
el=1
while n>=0:
    el=el/-2
    lst.append(el)
    n-=1
print(sum(lst))'''

def sum_elems(n, el):
    if n==0:
       return 0
    else:
       return el+sum_elems(n-1, el/-2)

print(sum_elems(4,1));