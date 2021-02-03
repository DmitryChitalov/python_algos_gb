"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
g_res = True

def check_n(in_n):
    if in_n == 1: return 1
    v_n = in_n + check_n(in_n-1)
    global g_res
    g_res= g_res and ( v_n == int(in_n * (in_n + 1) / 2))
    return v_n

if __name__ == '__main__':
    print('Input N:')
    v_n = int(input())
    v_chk = check_n(v_n)
    print('For N=' + str(v_n) + ' the result is ' + str(int(v_chk) == int(v_n * (v_n + 1) / 2)) )

    print('Recursive check is ' + str(g_res))
