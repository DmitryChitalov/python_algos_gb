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
some_users = {'user1':{'pswd':'1234', 'activated': True},
         'user2':{'pswd':'1234', 'activated': False},
         'user3':{'pswd':'1234', 'activated': True},
         'user4':{'pswd':'1234', 'activated': False}
         }
#линейная
def to_authorise (users, user_login, user_pswd):
    for key, value in users.items():  #O(N)
        if key == user_login:
            if value['pswd'] == user_pswd and value['activated'] == True:
                return ('Welcome!')
            elif value['pswd'] == user_pswd and value['activated'] == False:
                return ('You should activate your account')
            elif value['pswd'] != user_pswd:
                return ('Wrong password')
    return 'No such a user';

to_authorise(some_users, 'user3', '1234');

#Константная

def to_authorise_2 (users, user_login, user_pswd):
    if users.get(user_login):          #O(1)
        if users[user_login]['pswd'] == user_pswd and users[user_login]['activated']:
            print('Welcome!')
        elif users[user_login]['pswd'] == user_pswd and not users[user_login]['activated']:
            print ('You should activate your account')
        elif users[user_login]['pswd'] != user_pswd:
            print ('Wrong password')
        else:
            print('No such a user');

to_authorise_2(some_users, 'user1', '1234');