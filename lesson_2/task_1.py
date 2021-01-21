def calc():

    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':
        return 'Расчет окончен'
    else:
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            try:
                num_1, num_2 = (
                    int(input('Введите первое число: ')),
                    int(input('Введите второе число: '))
                    )
                if operation == '+':
                    print(f'Ваш результат: {num_1 + num_2}')
                    return calc()
                elif operation == '-':
                    print(f'Ваш результат: {num_1 - num_2}')
                    return calc()
                elif operation == '*':
                    print(f'Ваш результат: {num_1 * num_2}')
                    return calc()
                elif operation == '/':
                    if num_2 == 0:
                        print('Делить на 0 нельзя!')
                    else:
                        print(f'Ваш результат: {num_1 / num_2}')
                    return calc()
            except ValueError:
                print('Вы вместо числа ввели строку (((. Исправьтесь')
                return calc()
        else:
            print('Введен неверный символ')
            return calc()


calc()
