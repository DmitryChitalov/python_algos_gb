def recur_method(numb, s=0, m=1):

    print(s)
    if s == m:
        print(f'Равенство: {s == m}')
    elif s < m:
        return recur_method(numb, s + 1, numb * (numb + 1) // 2)


try:
    NUMB = int(input('Введите число: '))
    recur_method(NUMB)
except ValueError:
    print('Вы вместо числа ввели строку')
