"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def ask_number(message, invalid_number=[], invalid_number_message=""):
    pass
    invalid_number = list(invalid_number)
    res = input(message).strip()
    if not res.isdigit():
        return ask_number(message)
    elif res in invalid_number:
        print(invalid_number_message)
        return ask_number(message, invalid_number, invalid_number_message)

    if float(res) == int(res):
        return int(res)
    return float(res)


def ask_operation(message):
    pass
    valid_response = ["+", "-", "*", "/", "0"]
    res = input(message).strip()
    if res not in valid_response:
        print(f"Недопустимая операция!")
        res = ask_operation(message)
    return res


def do_calculate(arg1, arg2, operation):
    pass
    res = 0
    if operation == "+":
        res = arg1 + arg2
    elif operation == "-":
        res = arg1 - arg2
    elif operation == "*":
        res = arg1 * arg2
    elif operation == "/":
        res = arg1 / arg2

    if float(res) == int(res):
        return int(res)
    return float(res)


def loop():
    pass
    operation = ask_operation("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation == "0":
        return

    arg1 = ask_number("Введите первое число: ")

    if operation == "/":
        arg2 = ask_number("Введите второе число: ", "0", "Деление на ноль! Введите число отличное от нуля")
    else:
        arg2 = ask_number("Введите второе число: ")
    res = do_calculate(arg1, arg2, operation)
    print(f"Результат: {res}")
    loop()


def main():
    pass
    try:
        loop()
        print("Программа завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
