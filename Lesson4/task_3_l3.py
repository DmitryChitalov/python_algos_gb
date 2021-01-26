"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

# Рекурсию я переделала, мне кажется так как-то проще.
# Рекурсия
def revers(enter_num, revers_num=0):
    if enter_num//10==0:
        return (revers_num*10)+enter_num
    else:
        return revers(enter_num//10,(10*revers_num)+(enter_num%10))

# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

enter_num = int(input('Введите целое число: '))
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)

print(revers(enter_num))
print('Число наоборот на рекурсиях: ', timeit(f'revers({enter_num})',
                                               setup='from __main__ import revers', number=10000))
print('Число наоборот на циклах: ', timeit(f'revers_2({enter_num})',
                                            setup='from __main__ import revers_2', number=10000))
print('Число наоборот на срезах: ', timeit(f'revers_3({enter_num})',
                                            setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

"""
Применено 3 вида реализации задачи ( рекурсия, цикл, срез). 
Пример на моём компьютере:
Введите целое число: 3567891
1987653
Число наоборот на рекурсиях:  0.05218619900000121
Число наоборот на циклах:  0.03915716500000066
Число наоборот на срезах:  0.010067136999998283

Согласно полученным результатам видно что срез наиболее быстрый в плане выполнения
задачи. Рекурсия и цикл имеют арифмитические действия поэтому они проигрывают 
в скорости по сравнению со срезом в котором отсутствуют арифмитические действия.
Следовательно в подобных задачах оптимально использовать срез.
"""