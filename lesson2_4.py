def sum_row(n, start):
    if n == 0:
        return sum(temp_list)
    else:
        temp_list.append(start)
        start = -(start / 2)
        n -= 1
        return sum_row(n, start)


try:
    start = 1.0
    n = int(input('Введите количество элементов: '))
    temp_list = []
    print(f'Количество элементов: {n}, их сумма - {sum_row(n, start)}')
except ValueError:
    print('Ошибка, Введите целое положительное число')