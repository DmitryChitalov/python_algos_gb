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
def inverse_digit(a, num = ''):
    """ переворачивает число"""

    if a > 0:
        b = a // 10
        c = a - 10*b # получаем последнюю цифру
        num += str(c) # 
        return inverse_digit(b, num)
    else:
        return int(num)
    
        
    
    
        


if __name__ == "__main__":

    print(inverse_digit(3486))