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

even = []
even_count, not_even_count = 0, 0
not_even = []
try:
    user_number = int(input('Enter your number: '))


    def task_2(number):
        """
            Works only with integers (int).
        """
        global even, not_even, even_count, not_even_count
        if len(range(number)) == 0:
            print(
                f'Even numbers - {even}. Even cout - {even_count}\nNot even numbers - {not_even}. Even count - {not_even_count}')
        else:
            a = number % 10
            number = number // 10
            if a % 2 == 0:
                even.append(a)
                even_count += 1
                return task_2(number)
            else:
                not_even.append(a)
                not_even_count += 1
                return task_2(number)
except ValueError:
    print('Data error!')


task_2(user_number)