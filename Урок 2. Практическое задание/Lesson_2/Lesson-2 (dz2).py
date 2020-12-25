Количество четных и нечетных цифр в числе равно: (1, 2)
"""	"""


def numbers(num, even=0, odd=0):
    if num == 0 or num == -1:  # для отрицательного числа
        print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')
        return
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    return numbers(num//10, even, odd)


numbers(34560)