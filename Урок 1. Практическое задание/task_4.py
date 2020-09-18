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

user_db = [{'username': 'User_01', 'password': 'user_01_pass', 'acc_activated': True},
           {'username': 'User_02', 'password': 'user_02_pass', 'acc_activated': False},
           {'username': 'User_03', 'password': 'user_03_pass', 'acc_activated': True},
           {'username': 'User_04', 'password': 'user_04_pass', 'acc_activated': False},
           {'username': 'User_05', 'password': 'user_05_pass', 'acc_activated': True}
]
# вариант 1 сложность O(len(...)) (зависит от количества пользователей и позиции текущего пользователя в списке)


def user_auth(username):

    username_input = username
    for record in user_db:
        if username_input == record.get('username'):
            if not record.get('acc_activated'):
                print(f'пожалуйста, завершите активацию')
            else:
                password_input = input("Введите пароль:")
                if record.get('password') == password_input:
                    print(f'пользователь {username_input} авторизован')
                else:
                    print(f'неверный пароль')
            exit()
    print(f'пользователь {username_input} не найден')


# вариант 2 сложность O(len(...)) (производительность filter в строке 63 тоже зависит от количества пользователей)
# в варианте 2 заменил цикл for на lambda функцию с фильтром, однако, в целом, сложность остается на том же уровне.
# считаю, что варианты эквивалентны, но предпочтение у варианта 2, так как у варианта 1 с циклом код получился сложнее.


def user_auth2(username):

    username_input = username
    current_user = list(filter(lambda person: person['username'] == username_input, user_db))
    if not current_user:
        print(f'пользователь {username_input} не найден')
    else:
        if not current_user[0].get('acc_activated'):
            print(f'пожалуйста, завершите активацию')
        else:
            password_input = input("Введите пароль:")
            if current_user[0].get('password') == password_input:
                print(f'пользователь {username_input} авторизован')
            else:
                print(f'неверный пароль')


user_input = input('Введите имя пользователя:')

# для корректной работы функции user_auth2 вызов функции user_auth должен быть закомментирован (из-за exit() at line 53)

#user_auth(user_input)
user_auth2(user_input)
