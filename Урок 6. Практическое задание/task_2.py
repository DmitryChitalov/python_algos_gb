"""
Задание 2..
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
"""
Задание 3 *..
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile
@profile()
def func(x):
    even=0
    odd=0
    def even_odd(x, even, odd):

        if x == 0:
            return even, odd

        n = x % 10;
        if (n % 2 == 0):
            even = even + 1
        else:
            odd += 1;
        return even_odd(x // 10, even, odd)
    print(even_odd(x,even,odd))


even = 0
odd = 0
x = int(input("ведите число"))
print(func(x))
