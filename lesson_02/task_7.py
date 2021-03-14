"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def review(n, cur_elem=1, result_sum=0):
    if cur_elem > n:
        return result_sum
    result_sum += cur_elem
    cur_elem += 1
    return review(n, cur_elem, result_sum)


number = int(input('Введите любое натуральное число: '))
print(f'Сумма чисел от 1 до {number} равна {review(number)}\n'
      f'Выражение {number} * ({number} + 1) / 2 также равняется {number * (number + 1) / 2}')
