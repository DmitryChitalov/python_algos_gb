"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import collections
from memory_profiler import profile


@profile
def calc():
    companies_count = int(input("Введите количество предприятий: "))
    companies = collections.defaultdict()
    for i in range(companies_count):
        name = input(f"Введите название предприятия {i + 1}: ")
        profit = [int(input(f"Введите прибыль за {j + 1}-й квартал: ")) for j in range(4)]
        companies[name] = sum(profit)
        print(companies)

    avg = sum(companies.values()) / companies_count
    print(f"Средняя прибыль всех компаний за год: {avg}")

    for company in companies:
        print(company)
        if companies[company] >= avg:
            print(f"Компания: {company} имееет прибыль выше средней: {companies[company]}")
    for company in companies:
        if companies[company] < avg:
            print(f"Компания: {company} имеет прибыль ниже среднего: {companies[company]}")


@profile
def rec(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(rec(n // 10)))


## эта же задача на переверни число не рекурсией
@profile
def reverse():
    n1 = input("Введите целое число: ")
    n2 = n1[::-1]
    return print('"Обратное" ему число:', n2)


## тоже самое вайлом
@profile
def reverse_2():
    n1 = int(input("Введите целое число: "))
    n2 = 0
    while n1 > 0:
        digit = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + digit
    return print('"Обратное" ему число:', n2)


if __name__ == "__main__":
    calc()  ##функция крайне эффективная, использует всего 18.3 Mib без дальнейшего увеличения

    ## ниже видно, что вторая функция наиболее эффективная
    ##при вычислении огромных значений, Occurences не меняется
rec(2323131232131233232313123213123323231312321312332323131232131233)
reverse()
reverse_2()
