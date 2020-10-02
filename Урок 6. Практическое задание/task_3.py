"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile

@profile
def summa(a, num): # не больше 246 чисел можно ввести, иначе переполнение стека, при этом памяти расходуется всего 13.4 MiB
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

print(f'Сумма: {summa(s, n)}')