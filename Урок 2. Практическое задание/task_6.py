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
<<<<<<< Updated upstream
=======
from random import randint

def random_number(numb, count=10):
    rand_number = int(input('Enter number: '))
    count -= 1
    if count == 0:
        return f'Game over: the right number is : {numb}'
    elif numb == rand_number:
        return f'You won! Game over'
    elif numb > rand_number:
        print(f'The number is bigger, you have {count} tries')
        return random_number(numb, count)
    elif numb < rand_number:
        print(f'The number is  smaller, you have {count} tries')
        return random_number(numb, count)
    
numb = randint(1, 100)
print(random_number(numb))


>>>>>>> Stashed changes
