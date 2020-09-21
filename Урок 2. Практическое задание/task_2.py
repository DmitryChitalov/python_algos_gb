"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def even_uneven_count(number, even_count=0, uneven_count=0):

    if len(number) == 0:
        print (f'количество четных цфир:  {even_count}')
        print (f'количество нечетных цифр:{uneven_count}')
        return

    num = int(number[-1])

    if num%2 == 0:
        even_count +=1
    else:
        uneven_count +=1

    trimmed_str = number[:-1]
    even_uneven_count(trimmed_str, even_count,uneven_count)

user_input = str(4326981240)
print(f'введено число {user_input}')
even_uneven_count(user_input)
