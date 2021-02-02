"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random
g_tries = 10

def guess_num(in_num, in_tries):
    if in_tries==0:
        print('Sorry, you haven\'t guessed <' + str(in_num)+'>')
    else:
        print('Guess?')
        v_int = input()
        if v_int.isnumeric():
            if int(v_int) == in_num:
                print('You\'re right!')
                return;
            if int(v_int) > in_num:
                print('Try less!')
            if int(v_int) < in_num:
                print('Try more!')
        else:
            print('Please enter number!')
        guess_num(in_num, in_tries-1)

if __name__ == '__main__':
    v_int = random.randint(0, 100)
    guess_num(v_int,g_tries)

