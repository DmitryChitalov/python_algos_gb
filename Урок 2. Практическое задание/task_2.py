"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем 
соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def counter (count_num, even_value = 0, odd_value = 0) :
    list_num = list(count_num) 
    if int(list_num[-1]) % 2 == 0:
        even_value += 1
        list_num.pop(-1)
    else:   
        odd_value += 1
        list_num.pop(-1)
    if len(list_num) <= 0:
        return even_value, odd_value
    else:
        remains = int(count_num) // 10 
        return counter(str(remains), even_value, odd_value)

user_input = input('Введите Ваше число: ')
print(f'Колличество четных и ничетных цифр в Вашем числе: {counter(user_input)}')