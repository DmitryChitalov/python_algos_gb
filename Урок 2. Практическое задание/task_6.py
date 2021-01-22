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

num_1 = random.randint(0, 100)
print(num_1)


def random_num_generator(count, num_1):
    print(f"Attempt {count}")

    user_input = int(input("Guess the number from 0 to 100: "))
    if count == 10 or user_input == num_1:
        if user_input == num_1:
            print(f"Congratulations, you won!")
        print(f"Correct answer is: {num_1}")
    else:
        if user_input < num_1:
            print("Entered number is too small, try again: ")
        else:
            print("Entered number is too big, try again: ")
        random_num_generator(count + 1, num_1)


random_num_generator(1, num_1)
