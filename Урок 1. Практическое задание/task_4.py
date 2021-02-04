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

db = {'user1': {'password': 'password', 'activated': True},
      'user2': {'password': '123', 'activated': True},
      'user3': {'password': 'qwerty', 'activated': False}
      }


# Общая сложность O(n) т.к. используется один цикл
def login_1(users):
    lgn = input('Введите имя пользователя: ')
    pwd = input('Введите пароль: ')
    in_db = False
    for log, passwd in users.items():
        if log == lgn:
            if passwd['password'] == pwd and passwd['activated']:
                return 'Пользователь успешно вошел в систему'
            elif passwd['password'] == pwd and not passwd['activated']:
                return 'Пользователю необходимо активировать аккаунт!'
            else:
                return 'Неверный пароль!'
    return 'Пользователь не найден!'

# Общая сложность O(1) т.к. используется поиск по словарю
def login_2(users):
    lgn = input('Введите имя пользователя: ')
    pwd = input('Введите пароль: ')
    usr = users.get(lgn)
    if usr != None:
        if usr['password'] == pwd and usr['activated']:
            return 'Пользователь успешно вошел в систему'
        elif usr['password'] == pwd and not usr['activated']:
            return 'Пользователю необходимо активировать аккаунт!'
        else:
            return 'Неверный пароль!'
    return 'Пользователь не найден!'

#Второе решение эффективнее, т.к. имеет меньшую общую сложность

print(login_2(db))
