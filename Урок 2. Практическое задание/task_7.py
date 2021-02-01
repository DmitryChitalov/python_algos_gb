"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def check_naturls(i_num, i_i=1, i_sum=0):
    l_right = i_i*(i_i + 1)/2
    i_sum  += i_i
    #print('Debug', i_i, i_num, i_sum, l_right)

    if(i_sum != l_right):
        print(f'Проверка для числа {i_num} НЕ прошла!')
        return False

    if(i_i == i_num):
        return True

    return check_naturls(i_num, i_i+1, i_sum)

n = 10
print('Результат проверки:', check_naturls(n))
