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

def guess_number(count, number):

    input_answer = int(input('Please enter number from 0 to 100: '))
    if count == 10 or input_answer == number:
        if input_answer == number:
            print('You are lucky! Winner!')
        print(f'Number was {number}')
    else:
        if input_answer < number:
            print(f'Number is bigger then {input_answer}')
        else:
            print(f'Number is less then {input_answer}')
        guess_number(count + 1, number)



print('Welcome to program "Guess the number with usage recursion function"')
try:
    guess_number(1, random.randint(0,100))
except:
     print('Unknow Error! Try again.')
finally:
    print('Exit program.')