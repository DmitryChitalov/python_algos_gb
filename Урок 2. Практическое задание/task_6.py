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

import random as rd


class FindNum:

    def __init__(self):
        self.target_num = 0
        self.counter = 1

    def start(self):
        self.target_num = rd.choice(range(0, 101))
        print(self.target_num)
        self.ask()

    def ask(self):
        user_answer = int(input('Угадайте число от 0 до 100. Введите число: '))
        print(self.counter)
        if self.counter < 10:
            if user_answer == self.target_num:
                self.end('win')
            elif user_answer > self.target_num:
                self.counter += 1
                self.ask()
            else:
                print('Загаданное число больше')
                self.counter += 1
                self.ask()
        else:
            self.end('lose')

    def end(self, result):
        if result == 'win':
            print(f'Вы угадали число за {self.counter} попыток')
        else:
            print(f'Вы не угадали число за 10 попыток')


game = FindNum()
game.start()