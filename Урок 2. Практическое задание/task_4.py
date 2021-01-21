"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def summary_recurs (us_ip, start_param = 1, param_lst = []):
    if us_ip >= 0: 
        start_param /= 2
        param_lst.append(start_param)
        us_ip -= 1
        return summary_recurs (us_ip, start_param)
    else:
        return float(sum(param_lst))

user_input = int(input('Введите колличество элементов: '))
print(f'Количество элементов - {user_input}, их сумма - {summary_recurs(user_input)}')