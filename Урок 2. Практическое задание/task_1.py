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
print("= " * 50)
print("{greeting:^100}".format(greeting="Программа Калькулятор!"))
print("= " * 50)

oper_symbol = ['+', '-', '*', '/']
next_inter = True

print("Введите операцию:")

def do_calc(oper_sym, input_number_1, input_number_2) -> float:

    oper_sym = input("(+, -, *, / или 0 для выхода): ")
    res = 0
    if oper_sym == '0':
        print("[INFO] Завершение программы...")
        return -1

    if oper_sym not in oper_symbol:
        print(f'Ошибка ввода: введеный знак операции "{oper_sym}" не поддерживается. повторите еще раз.\n')
        oper_sym = ''
    else:
        if not input_number_1:
            input_number_1 = input(f"Введите первое число: ")

        if input_number_1.isdigit():
            if not input_number_2:
                input_number_2 = input(f"Введите второе число: ")
                if input_number_2.isdigit():
                    if oper_sym == '+':
                        res = float(float(input_number_1) + float(input_number_2))
                    elif oper_sym == '-':
                        res = float(float(input_number_1) - float(input_number_2))
                    elif oper_sym == '*':
                        res = float(float(input_number_1) * float(input_number_2))
                    elif oper_sym == '/' and int(input_number_2) != 0:
                        res = float(float(input_number_1) / float(input_number_2))
                    else:
                        print(f"Ошибка ввода: второе значение равно {input_number_2}.")
                else:
                    print(f"Ошибка ввода: второе значение {input_number_2} не является числом - повторите попытку\n")
                    input_number_2 = ''
                    do_calc(oper_sym, input_number_1, input_number_2)
        else:
            print(f"Ошибка ввода: значение {input_number_1} не является числом - повторите попытку\n")
            input_number_1 = ''
            do_calc(oper_sym, input_number_1, input_number_2)

    return res

while next_inter:
    operation = ''
    input_number_1 = ''
    input_number_2 = ''

    result = do_calc(operation, input_number_1, input_number_2)

    print(f"Результат операции: {result}\n")

    while True:
        next_add = input("Хотите выполнить дополнительный расчет (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")
