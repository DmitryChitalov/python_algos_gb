"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Найти сумму (n) элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."))
print("= " * 50)

next_inter = True


def do_summa(p_idx, p_priv):
    if p_idx == -1:
        vsrt = input("Введите целочисленное число: ")
        print("Введено: " + vsrt)
        if vsrt == '':
            vsrt = -2

        g_res['sum'] = 0
        g_res['n'] = int(vsrt)
        p_idx = g_res['n']

    if p_idx == None or p_idx == -2:
        print("Количество элементов не определено. Пока!")
        return
    else:
        if p_idx == 0:
            print("\nРезультат: " + str(g_res['sum']))
            do_summa(-1, -2)
        else:
            p_priv = (p_priv * -0.5)
            p_idx = p_idx - 1
            print(str(p_priv) + '; ', end='')
            g_res['sum'] = g_res['sum'] + p_priv
            do_summa(p_idx, p_priv)


while next_inter:
    g_res = {'sum': 0, 'n': 0}
    do_summa(-1, -2)
    while True:
        next_add = input("Хотите продолжить (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")
