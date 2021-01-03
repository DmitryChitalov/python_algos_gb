"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = int(input("Введите число "))
print(f"Проверяем что все работает - {revers(num)}")
print(f"Проверяем что все работает - {revers_2(num)}")
print(f"Проверяем что все работает - {revers_3(num)}")

# Умножаем на 100 чтобы было удобнее смотреть на полученный результат

elapsed_recurs = (timeit.timeit("revers(num)",
                                setup="from __main__ import revers, num",
                                number=10000)) * 100
elapsed_for = (timeit.timeit("revers_2(num)",
                             setup="from __main__ import revers_2, num",
                             number=10000)) * 100
elapsed_slice = (timeit.timeit("revers_3(num)",
                               setup="from __main__ import revers_3, num",
                               number=10000)) * 100
print(f"Время с рекурсией - {elapsed_recurs}\n"
      f"Время с циклом - {elapsed_for}\n"
      f"Время со срезом - {elapsed_slice}")

cProfile.run('revers(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

# ----------------------------ВЫВОДЫ------------------------------------
# Очевидно что рекурсия самая ресурсоемкая, серебро взял цикл, ну и соот-
# ветственно срез сегодня у нас чемпион, так как это встроенная функция!
