"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def count_odd_even(number, odd = 0, even= 0):
    # Function use recursion
    if number == 0:
        return odd, even
    else:
        current_number  = number % 10
        number = number // 10
        if current_number % 2 != 0:
            odd += 1
            return count_odd_even(number, odd, even)
        else:
            even += 1
            return count_odd_even(number, odd, even)

print('Welcome to program "Count odd and even in number with usage recursion function"')
try:
    input_number = int(input('Please enter int number: '))
    print(f'Numbers of odd and even in entered number {count_odd_even(input_number)}')
except ValueError:
    print('Error! Value error! Please, check that you enter number!')
except:
    print('Unknow Error! Try again.')
finally:
    print('Exit program.')