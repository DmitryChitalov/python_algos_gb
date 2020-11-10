"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""

def do_reverse_number(number, reverse = 0):

    if number == 0:
        return reverse
    else:
        reverse = (reverse * 10) + (number % 10)
        number = number // 10
        return do_reverse_number(number, reverse)

print('Welcome to program "Do reverse number with usage recursion function"')
try:
    input_number = int(input('Please enter int number: '))
    print(f'After reverse your number is: {do_reverse_number(input_number)}')
except ValueError:
    print('Error! Value error! Please, check that you enter number!')
except:
    print('Unknow Error! Try again.')
finally:
    print('Exit program.')

