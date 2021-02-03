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

user_dict = {"user1": {
    "password": "test1", "activated": 0
}, "user2": {
    "password": "test2", "activated": 0
}, "user3": {"password": "test3", "activated": 1}}


def search_user(login):  # O(1)
    try:
        a = user_dict[login]
        return True
    except KeyError:
        return False


def validate_password(login, password):  # O(1)
    try:
        if password == user_dict[login]['password']:
            return True
        else:
            return False
    except KeyError:
        return False


def activate_user(login):  # O(1)
    user_dict[login]['activated'] = 1


def variant1():
    user_input_login = str(input("Введите логин ==>"))

    # checking login
    if search_user(user_input_login):
        user_input_password = str(input("Введите пароль ==>"))
        if validate_password(user_input_login, user_input_password):
            print('пароль принят. Проверка активации пользователя')
            if user_dict[user_input_login]['activated'] == 0:
                user_acces = str(input("Пользователь не активирован. Вы хотите активировать пользователя? Yy/nN"))
                if user_acces.lower() == 'y':
                    activate_user(user_input_login)
                    print('Учетная запись активирована. Приятного пользования')
                    print(user_dict)
                    exit()
                if user_acces.lower() == 'n':
                    print('Вы отказались от активации пользователя. Выход')
                else:
                    print("Введен неправльный символ подтверждения. Выход")
            else:
                print('Вы успешно зашли на ресурс. Приятного пользования')
        else:
            print('не правильный пароль. Выход')
    else:
        print('Пользователь не найден')


# решение 2

def check_user(login):
    for i in user_dict:
        if i == login:
            return True
    return False


def check_password(login, password): #O(n^2)
    for i in user_dict: #O(n)
        if i == login:
            for k in user_dict[i]: #O(n)
                if k == "password":
                    if password == user_dict[i][k]:
                        return True
                    else:
                        return False
    return False

def activate(login):
    user_dict[login]['activated'] =1

def variant2():
    ittr_user = 0
    login = ''
    password = ''
    while ittr_user < 3:
        user_input_login = str(input("Введите логин ==>"))
        if check_user(user_input_login):
            login = user_input_login
            break
        else:
            print('не верный пользователь. Попробуй снова')
        ittr_user += 1
    ittr_pass = 0

    while ittr_pass < 3:
        user_input_password = str(input("Введите пароль ==>"))
        if check_password(login, user_input_password):
            print('пароль принят. Проверка валидации')
            if user_dict[login]['activated'] == 1:
                print('Вы успешно зашли на ресурс. Приятного пользования')
                print(user_dict)
                exit()
            else:
                user_acces = str(input("Пользователь не активирован. Вы хотите активировать пользователя? Yy/nN"))
                if user_acces.lower() == 'y':
                    activate_user(login)
                    print('Учетная запись активирована. Приятного пользования')
                    print(user_dict)
                    exit()
                if user_acces.lower() == 'n':
                    print('Вы отказались от активации пользователя. Выход')
                    exit()
                else:
                    print("Введен неправльный символ подтверждения. Выход")
                    exit()

        else:
            print('Не правильный пароль. Попробуйте еще раз')
        ittr_pass += 1
variant1() #O(1) -
variant2() #O(n^2)