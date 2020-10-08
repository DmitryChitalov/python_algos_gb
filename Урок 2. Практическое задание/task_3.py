"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""
next_inter = True


def revers_str(p_str, p_idx):
    if p_str == '-':
        vsrt = input("Введите число: ")
        print(vsrt)
        g_res['revers'] = ''
    else:
        vsrt = p_str

    if len(vsrt) == 0 or vsrt == None or vsrt == '':
        print("Строка не определена. Пока!")
        return
    else:
        if len(vsrt) <= p_idx:
            print("Обратка: " + str(g_res['revers']))
            revers_str('-', 0)
        else:
            g_res['revers'] = vsrt[p_idx] + g_res['revers']
            p_idx = p_idx + 1
            revers_str(vsrt, p_idx)


while next_inter:
    g_res = {'revers': ''}
    revers_str('-', 0)
    while True:
        next_add = input("Хотите продолжить (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")
