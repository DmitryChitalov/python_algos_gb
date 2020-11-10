"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

"""

def sum_of_elements(count, number, count_el, sum_el):
    if count == count_el:
        print(f'Number of elements: {count_el}, sum: {sum_el}')
    elif count < count_el:
        return sum_of_elements(count + 1, number / 2 * -1, count_el, sum_el + number)

print('Welcome to program "Find summ of elements with usage recursion function"')
try:
    value_elements = int(input('Please enter value of elements: '))
    sum_of_elements(0, 1, value_elements, 0)
except ValueError:
    print('Error! Value error! Please, check that you enter number!')
except:
    print('Unknow Error! Try again.')
finally:
    print('Exit program.')