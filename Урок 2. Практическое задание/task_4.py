"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def input_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit() or not res.isdecimal():
        print("Недопустимый ввод!")
        res = input_number(message)

    return res


def do_calc(number, steps):
    pass
    steps -= 1
    if steps < 0:
        return 0
    res = float(number) / 2 * -1
    print(f"step: {steps}, res = {res}")
    res += do_calc(res, steps)
    return res


def main():
    pass
    try:
        number = 1
        steps = int(input_number("Введите количество элементов(целое число): "))
        res = do_calc(number, steps)
        print(f"Количество элементов - {steps}, их сумма - {res}")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
