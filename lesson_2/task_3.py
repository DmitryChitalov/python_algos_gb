def revers_number(numb):

    if len(numb) == 1:
        return numb
    else:
        return str(int(numb) % 10) + revers_number(str(int(numb) // 10))


number = input('Введите число, которое требуется перевернуть: ')
print(f'Перевернутое число: {revers_number(number)}')
