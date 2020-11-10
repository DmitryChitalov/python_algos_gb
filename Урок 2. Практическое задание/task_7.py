"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def check_equation(number, a = 0, b = 1):

    if a == b:
        print(f'A == B  {a == b}')

    elif a < b:
        return check_equation(number, a + 1, number * (number + 1) // 2)

try:
    input_number = int(input('Please enter number: '))
    check_equation(input_number)
except ValueError:
    print('Error! Value error! Please, check that you enter number!')
except:
     print('Unknow Error! Try again.')
finally:
    print('Exit program.')
