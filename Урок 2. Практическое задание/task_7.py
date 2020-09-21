"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def check_equation(elements_quantity, initial_qty, sum_of_elements=0, next_element = 1):
    elements_qty = elements_quantity
    initial_elements_qty = initial_qty

    if elements_qty == 0:
        print (f'результат прямого пересчета суммы элементов:{sum_of_elements}')
        print (f'результат вычисления по формуле n(n+1)/2   :{initial_elements_qty*(initial_elements_qty+1)/2}')
        return

    sum_of_elements = sum_of_elements + next_element
    next_element += 1

    elements_qty -=1
    check_equation(elements_qty, initial_elements_qty, sum_of_elements,next_element)


input_number_of_elements = 9
check_equation(input_number_of_elements, input_number_of_elements)