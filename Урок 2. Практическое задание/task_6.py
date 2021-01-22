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

found_number = randint(1, 101)
f = str(f'--TOP-SECRET-NUM-{found_number}--')
print(f)  # Выводит искомое число, по дефолту disabled


def task_6(trys_count=10):
    """
        Функция принимает ввод и сравнивает со сгенерированным числом.
        q - выход.
        # в целом мне алгоритм кажется хорошим, но есть одна досадная ошибка, но всё работает.
    """
    global found_number, f
    user_numper = input(
        f'{"-" * len(f)}\nYou have {trys_count} attempts.\nEnter your number in range [1: 100], or "q" to exit: ')
    if user_numper != 'q':
        try:
            user_numper = int(user_numper)
            if trys_count > 1:
                # print(f'fn - {found_number}, un - {user_numper}, tk - {trys_count}')
                if found_number == user_numper:
                    print(f'{"-" * len(f)}\n- Correct! {found_number}!\n{f}')
                    return
                elif found_number < user_numper:
                    print(f'{"-" * len(f)}\n- No, you need a smaller (<{user_numper}) number.')
                    return task_6(trys_count - 1)
                else:
                    print(f'{"-" * len(f)}\n- No, you need a bigger (>{user_numper}) number.')
                    return task_6(trys_count - 1)
            else:
                print(f'{"*" * len(f)}\nFin.\n{f}')
                return
        except ValueError:
            print(f'{"-" * len(f)}\n- You should type only digits.')
            return task_6(trys_count - 1)


task_6()


# attempt 2 (GB method)
def recur_method(count, numb):
    print(f'Attempt {count}')
    answer = int(input('Enter your number in range [1: 100]: '))
    if count == 10 or answer == numb:
        if answer == numb:
            print('Correct!')
        print(f'The number is {numb}')
    else:
        if answer > numb:
            print(f'No, you need a smaller (<{answer}) number.')
        else:
            print(f'No, you need a bigger (>{answer}) number.')
        recur_method(count + 1, numb)

recur_method(1, randint(0, 100))
