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
def game_for_user (user_inp, count_try_def, prog_num = random.randrange(100)):
    try: 
        if user_inp == prog_num:
            print('Вы угадали')
            return
        elif count_try_def == 10:
            print (f'Вы проиграли. Загаданное число == {prog_num}')
        elif user_inp != prog_num and count_try_def < 10:
            if user_inp < prog_num:  # эта проверка появилас после того, как внимательнее перечитал задание и увидел условие о подсказке </>. не стал переписывать весь код, но добавил лишний блок.
                rep_user_input = int(input((f'Вы не угадали. Ваше число "<" загаданного. Осталось {10-count_try_def} попыток. Вводите число: ')))
                count_try_def += 1
            else:
                rep_user_input = int(input((f'Вы не угадали. Ваше число ">" загаданного. Осталось {10-count_try_def} попыток. Вводите число: ')))
                count_try_def += 1
            return game_for_user(rep_user_input, count_try_def)
    except ValueError:
        print('Введите число в формате "123", а не прописью: ')
        game_for_user(user_input, count_try_from_sys)

try:
    user_input = int(input('Играем в игру "угадайка". Программа загадала число. Угадайте его.\nВведите Ваше число: '))
except ValueError:
    user_input = int(input('Введите число в формате "123", а не прописью: '))
count_try_from_sys = 1
game_for_user(user_input, count_try_from_sys)
