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


from random import randint


def generated_number(answer, attempt=10):
    if attempt == 0:
        print(f'Все попытки кончились, было загадано {answer}')
        return

    user_answer = input('Угадайте число: ')
    if user_answer.isdigit():
        user_answer = int(user_answer)

        attempt -= 1
        if answer == user_answer:
            print(f'Ура, Вы угадали!!!')
        elif answer > user_answer:
            print(f'Загаданное число больше (осталось {attempt} попыток)')
            return generated_number(answer, attempt)
        elif answer < user_answer:
            print(f'Загаданное число меньше (осталось {attempt} попыток)')
            return generated_number(answer, attempt)

    else:
        print('Введите число!')
        return generated_number(answer, attempt)


answer_data = randint(0, 100)
generated_number(answer_data)