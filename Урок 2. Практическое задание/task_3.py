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
#num = int(input('Введите число, которое требуется перевернуть:'))

#было так, но посмотрев пример - переписала.
def reverse_num(num):
    if num == 0:
        return
    else:
        dig=num%10
        num=num//10
        print(dig)
    return reverse_num(num)

#print(reverse_num(654));

