"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""

# Дмитрий, я понимаю, что отклонился от задания, но зацените, по-моему очень элегантно получилось.

def task_3():
    """
        Функция производит "разворот" целочисленного занчения.
        q - exit
    """
    us_num = input('Your number (or "q" to exit): ')
    if us_num.lower() == "q":
        return 'Fin.'
    else:
        us_num_copy = us_num[::-1]
        try:
            us_num_copy_int = int(us_num_copy)
            print(f'Your reversed number: {us_num_copy_int}')
            return task_3()
        except ValueError:
            print('Data error!')
            return task_3()


print(task_3())


# attempt 2 (GB method)
def revers_number(numb):
    if len(numb) == 1:
        return numb
    else:
        return str(int(numb) % 10) + revers_number(str(int(numb) // 10))

user_number = input('Enter your number: ')
print(f'Your reversed number: {revers_number(user_number)}')
