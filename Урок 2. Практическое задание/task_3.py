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


def reverse_number(number, postion):
    pass
    res = ""
    postion -= 1
    if postion < 0:
        return res

    res = number[postion]
    res += reverse_number(number, postion)

    return res


def input_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit():
        print("Недопустимый ввод!")
        res = input_number(message)

    return res


def main():
    pass
    try:
        number = input_number("Введите число, которое требуется перевернуть: ")
        res = reverse_number(number, len(number)).strip()
        print(f"Перевернутое число: {res}")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
