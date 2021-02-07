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


def count(string: int):
    if string // 10 == 0:
        if string % 2 == 0:
            return [1, 0]
        else:
            return [0, 1]
    else:
        head = string // 10
        tail = string % 10
        if tail % 2 == 0:
            summary=count(head)
            summary[0]+=1
        else:
            summary = count(head)
            summary[1] += 1
        return summary

value=12413185
result=count(value)

print(f'Число четных и нечетных цифр в числе {value} составляет {result[0]} и {result[1]} соответственно')