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

my_dict = {
    'user_1': {
        'password': '12345',
        'activation': True
    },
    'user_2': {
        'password': '12345',
        'activation': False
    },
    'user_3': {
        'password': '12345',
        'activation': True
    },
    'user_4': {
        'password': '12345',
        'activation': False
    }
}

#1
#сложность О(N^2)


def alg_1(users, login, password):
    if login in users.keys():
        for key, value in users.items():
            if key == login:
                if value.get('activation') == True and value.get(
                        'password') == password:
                    return f'{login}, добро пожаловать!'
                elif value.get('activation') == False and value.get(
                        'password') == password:
                    return f'{login}, пройдите активацию учетной записи'
                elif (value.get('activation') == True
                      or value.get('activation') == False
                      ) and value.get('password') != password:
                    return f'{login}, вы ввели не верный пароль!'
    else:
        return f'Пользователя не существует!'


print(alg_1(my_dict, 'user_1', '12345'))

#2
#сложность О(1)


def alg_2(users, login, password):
    if users.get(login):
        if users[login]['activation'] == True and users[login][
                'password'] == password:
            return f'{login}, добро пожаловать!'
        elif users[login]['activation'] == False and users[login][
                'password'] == password:
            return f'{login}, пройдите активацию учетной записи'
        elif (users[login]['activation'] == True
              or users[login]['activation'] == False
              ) and users[login]['password'] != password:
            return f'{login}, вы ввели не верный пароль!'
    else:
        return f'Пользователя не существует!'


print(alg_2(my_dict, 'user_1', '12345'))
"""
Благодаря тому что избавляемся от 2х циклов в 1 алгоритме, значительно упрощаем структуру и сложность, поэтому вариант под номером 2 является оптимальным.
"""
