"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым


from timeit import timeit
def recursive_reverse(number):

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
#num_10000 = randint(100000000, 10000000000000)
num_10000 = randint(100000000000000000000000, 1000000000000000000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
def recursive_reverse_mem(number):
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


######################################################################################################
print()
print("######### Попытки оптимизации ##################")

def reverse_str(num): # через индексы строки
    num = str(num)
    revers_num = num[::-1]
    return revers_num

def divide_num(num): # используем целое и остаток от деления
    m = 0
    while num > 0:
        m = m * 10 + num % 10
        num = num // 10
    return m

def lambda_reverse(num): # используем lambda
    return num[::-1]
lambda_reverse = lambda num: num[::-1]

print("через индексы строки")
print(timeit('reverse_str(num_100)',setup='from __main__ import reverse_str, num_100',number=10000))
print(timeit('reverse_str(num_1000)',setup='from __main__ import reverse_str, num_1000',number=10000))
print(timeit('reverse_str(num_10000)',setup='from __main__ import reverse_str, num_10000',number=10000))

print()
print("используем целое и остаток от деления")
print(timeit('divide_num(num_100)',setup='from __main__ import divide_num, num_100',number=10000))
print(timeit('divide_num(num_1000)',setup='from __main__ import divide_num, num_1000',number=10000))
print(timeit('divide_num(num_10000)',setup='from __main__ import divide_num, num_10000',number=10000))

print()
print("используем labmda")
num_100=str(num_100)
num_1000=str(num_1000)
num_10000=str(num_10000)
print(timeit('lambda_reverse(num_100)',setup='from __main__ import lambda_reverse, num_100',number=10000))
print(timeit('lambda_reverse(num_1000)',setup='from __main__ import lambda_reverse, num_1000',number=10000))
print(timeit('lambda_reverse(num_10000)',setup='from __main__ import lambda_reverse, num_10000',number=10000))

"""
Мемоизация быстрее рекурсии, не надо вычислять каждый раз предыдущее значения, оно уже есть в памяти
В данном случае имеет смысл к существованию.
Попробовал оптимизировать применив другие алгоритмы: по индексу строки / по целому и остатку.
Эти варианты по скорости сопоставимы с рекурсией.
Лучший алгоритм получился - используя lambda.
Ниже результат по num_10000, как наиболее затратный у всех алгоритмов:
    Не оптимизированная функция recursive_reverse
    0.15688069999999998
    Оптимизированная функция recursive_reverse_mem
    0.006145899999999982
    
    ######### Попытки оптимизации ##################
    через индексы строки
    0.008797499999999958
    
    используем целое и остаток от деления
    0.099968
    
    используем labmda
    0.002445799999999998
""" 
