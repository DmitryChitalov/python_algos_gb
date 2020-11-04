"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
import hashlib

users = {'qwerty': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}  # пароль '123'
activated = {'qwerty': True}


# Решение №1 (сложность O(n^2)):
def check_users_1():
    def registration():
        while True:
            login = input('Логин: ')
            if login.lower() not in users.keys():
                password = input('Пароль: ')
                pass_hash = hashlib.sha256(password.encode())
                users[login.lower()] = pass_hash.hexdigest()
                activated[login.lower()] = False
                break
            else:
                print(f'\nИмя пользователя уже занято, пожалуйста выберите другое.\n')

    def check():
        login = input('Логин: ')
        password = input('Пароль: ')
        pass_hash = hashlib.sha256(password.encode()).hexdigest()
        if login.lower() in users.keys():

            for usr_key in users.keys():
                if login.lower() == usr_key:
                    if pass_hash == users[usr_key]:
                        for act_key in activated.keys():
                            if login.lower() == act_key:
                                if activated[act_key] == True:
                                    print(f'\nДоступ разрешён: аутентификация пройдена.\n')
                                else:
                                    if input(f'\nДоступ ограничен:'
                                             f' активируйте вашу учётную запись. '
                                             f'Проверьте ваш почтовый ящик.\n'
                                             f'Отправить письмо повторно? (y/n)\n') in ('y', 'н'):
                                        print('Письмо с и инструкцией об активации '
                                              'было отправлено на ваш почтовый ящик')
                                    else:
                                        break
        else:
            print(f'\nПользователь не найден.\n')

    while True:
        user_input = input('Нажмите E для входа, R для регистрации или Q для выхода: ')

        if user_input.lower() in ('e', 'у'):
            print(f'\nВход в учётную запись: \n')
            check()
        elif user_input.lower() in ('r', 'к'):
            print(f'\nРегистрация новой учётной записи: \n')
            registration()
            print()
        elif user_input.lower() in ('q', 'й'):
            print(f'\nВыход')
            break
        else:
            print(f'Ошибка ввода. Повторите ввод.\n')


# Решение №2 (сложность O(n)):
# Учитывая сложность O и длину кода, это решение лучшее из представленных.
def check_users_2():
    while True:
        user_input = input(f'\nВведите E для входа, R для регистрации или Q для выхода: \n')
        if user_input.lower() in ('q', 'й'):
            break
        elif user_input.lower() in ('e', 'r', 'к', 'у'):
            login = input('логин: ')
        else:
            print(f'\nОшибка ввода. Повторите ввод ещё раз.\n')
            continue
        if login.lower() in users.keys() and users[login.lower()] == hashlib.sha256(
                input('Пароль: ').encode()).hexdigest():
            if activated[login.lower()] == True:
                print(f'\nДоступ разрешён: аутентификация пройдена.\n')
            else:
                if input(f'\nДоступ ограничен:'
                         f' активируйте вашу учётную запись. '
                         f'Проверьте ваш почтовый ящик.\n'
                         f'Отправить письмо повторно? (y/n)\n') in ('y', 'н'):
                    print(f'Письмо с и инструкцией об активации '
                          f'было отправлено на ваш почтовый ящик')

        else:
            if user_input.lower() in ('r', 'к'):
                users[login.lower()] = hashlib.sha256(input('Пароль: ').encode()).hexdigest()
                activated[login.lower()] = False
                continue
            else:
                print('Пользователь не найден.')


# Решение №3 (сложность O(n)):
def check_users_3():
    while True:
        user_input = input(f'\nВведите E для входа, R для регистрации или Q для выхода: \n')

        if user_input.lower() in ('e', 'у'):
            login = input('Логин: ')
            pass_hash = hashlib.sha256(input('Пароль: ').encode()).hexdigest()
            if login.lower() in users.keys() and activated[login.lower()] == True:
                print('Активация пройдена.')
            elif login.lower() in users.keys() and activated[login.lower()] == False:
                if input(f'\nДоступ ограничен:'
                         f' активируйте вашу учётную запись. '
                         f'Проверьте ваш почтовый ящик.\n'
                         f'Отправить письмо повторно? (y/n)\n') in ('y', 'н'):
                    print(f'Письмо с и инструкцией об активации '
                          f'было отправлено на ваш почтовый ящик')
            elif login.lower() not in users.keys() or users[login.lower()] != pass_hash:
                print(f'\nОшибка в имени пользователя и/или пароле, либо учётной записи не существует.\n')
        elif user_input.lower() in ('r', 'к'):
            while True:
                login = input('login: ')
                if login.lower() in users.keys():
                    print(f'\nИмя пользователя уже занято, пожалуйста выберите другое.\n')
                else:
                    users[login.lower()] = hashlib.sha256(input('Пароль: ').encode()).hexdigest()
                    activated[login.lower()] = False
                    print(f'\nВнимание! '
                          f'После регистрации вам необходимо активировать '
                          f'учётную запись при помощи электронного письма.\n')
                    break
        elif user_input.lower() in ('q', 'й'):
            break
        else:
            print(f'Ошибка ввода. Повторите ввод.\n')
            continue


# check_users_1()
check_users_2()
# check_users_3()
