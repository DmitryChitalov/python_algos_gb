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

def guess_num(n, try_count=10):
    #print (n)
    user_answer = int(input('enter a digit from 1 to 100'))
    if try_count==0:
        print('Game over')
    elif user_answer == n:
        print(f'You win, number is {n}')
    elif user_answer > n:
        print(f'Your answer is too big, you have {try_count-1} tries left')
        guess_num(n,try_count-1)
    else:
        print(f'Your answer is too small, you have {try_count-1} tries left')
        guess_num(n,try_count-1)


print(guess_num(random.randint(0,100)));
