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


def reverse_list(**data):
    try:
        data_list = data['user_inp']
        data_rev = data['reverse_d']
        if len(data_list) == 1:
            data_rev.append(data_list[0])
            return data_rev
        else:
            data_rev.append(data_list.pop())
            return reverse_list(user_inp=data_list, reverse_d=data_rev)

    except ValueError:
        print('str value! Pls try again')
        return reverse_list(user_inp=list(input('Your value: ')), reverse_d=[])


user_inp = list(input('Your value: '))
print(reverse_list(user_inp=user_inp, reverse_d=[]))
