from random import randint

rand = randint(0, 101)
count = 1


def guess_numb(n):
    global count
    if count == 11:
        return f'Попытки закончились, число {n}'
    else:
        answer = int(input(f'попытка {count}, введите число: '))
        count += 1
        if answer < n:
            print('Число меньше загаданного')
            return guess_numb(n)
        elif answer > n:
            print('Число больше загаданного')
            return guess_numb(n)
        else:
            return f'Вы угадали! попыток {count}!'


print(guess_numb(rand))
