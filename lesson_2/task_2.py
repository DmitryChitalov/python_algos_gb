def recur_method(numb, even=0, odd=0):

    if numb == 0:
        return even, odd
    else:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return recur_method(numb, even, odd)


try:
    NUMB = int(input('Введите натуральное число'))
    print(f'Количество четных и нечетных цифр в числе равно: {recur_method(NUMB)}')
except ValueError:
    print('Вы вместо числа ввели строку')
