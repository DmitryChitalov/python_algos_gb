"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def natural_input():
    __natural = input('Введите количество элементов: ')
    try:
        return int(__natural)
    except:
        print('Вы ввели не число')
        return natural_input()

def sequence_sum(seq_len,curr_elem=1, sum=0):
    if(seq_len == 0):
        return sum
    else:
        return sequence_sum(seq_len-1,-1*curr_elem/2,sum+curr_elem)

n = natural_input()
print(f'Количество элементов - {n}, их сумма - {sequence_sum(n)}')
