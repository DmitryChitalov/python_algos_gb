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


def fun(a):
    if a == 0:
        return
    print(a % 10, end='')
    a = a // 10
    fun(a)


a = int(input('Введите число, которое требуется перевернуть:   '))
print('Перевернутое число: ', end='')
fun(a)