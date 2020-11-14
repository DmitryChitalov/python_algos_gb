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


def user_authorise():
    user = [input('Введите логин: '), input('Введите pwd: ')]
    return user

# Вариант 1. O(3n) В общем плохой вариант т.к. сложность очень высокая
def autentif_user_1(user):
    for j, k in user_data.items():
        if j == user[0]:
            if k.get('pass') == user[1]:
                if k.get('active') == 'yes':
                    print(f'Добро пожаловать в систему, {j}!')
                    break
                else:
                    print(
                        f'{j}, ваша учетная запись не активирована. Для доступа к ресурсу пройдите пожалуйста активацию!')
                    break
    else:
        print('Неправильный логин или пароль!')


# Вариант 2. O(2n). Вариант лучше 1-го. т.к. получилось избежать 1-ой вложенности и уменьшить сложность.
def autentif_user_2(user):
    for j, k in user_data.items():
        if j == user[0] and k.get('pass') == user[1]:
            if k.get('active') == 'yes':
                print(f'Добро пожаловать в систему, {j}!')
                break
            else:
                print(
                    f'{j}, ваша учетная запись не активирована. Для доступа к ресурсу пройдите пожалуйста активацию!')
                break
    else:
        print('Неправильный логин или пароль!')


user_data = {'Alex': {'pass': '12345', 'active': 'yes'},
             'Max': {'pass': '54321', 'active': 'no'},
             'Piter': {'pass': 'qwert', 'active': 'yes'},
             'Joe': {'pass': 'Joe1999', 'active': 'no'},
             'Kat': {'pass': '0415Kat', 'active': 'yes'}
             }


user = user_authorise()
autentif_user_1(user)
autentif_user_2(user)
