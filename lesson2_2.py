def check_even_odd(num, even=0, odd=0):
    if num == 0:
        return f'Четных чисел - {even}\nНечетных чисел - {odd}'
    elif (num % 10) % 2 == 0:
        return check_even_odd(num // 10, even + 1, odd)
    else:
        return check_even_odd(num // 10, even, odd + 1)


while True:
    try:
        num = int(input('Введите целое число'))
        print(check_even_odd(num))
        break
    except ValueError:
        print(f'Ошибка, Введите целое положительное число')
