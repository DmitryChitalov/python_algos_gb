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
При этом его учётка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

DATABASE1 = {
    "user_1": {"password": "password1", "is_activated": 1},
    "user_2": {"password": "password2", "is_activated": 0},
    "user_3": {"password": "password3", "is_activated": 1},
    "user_4": {"password": "password4", "is_activated": 0},
    "user_5": {"password": "password5", "is_activated": 1},
    "user_6": {"password": "password6", "is_activated": 0},
    "user_7": {"password": "password7", "is_activated": 1},
    "user_8": {"password": "password8", "is_activated": 0},
    "user_9": {"password": "password9", "is_activated": 1},
    "user_10": {"password": "password10", "is_activated": 0},
    "user_11": {"password": "password11", "is_activated": 1},
}

DATABASE2 = [
    {"login": "user_1", "password": "password1", "is_activated": 1},
    {"login": "user_2", "password": "password2", "is_activated": 0},
    {"login": "user_3", "password": "password3", "is_activated": 1},
    {"login": "user_4", "password": "password4", "is_activated": 0},
    {"login": "user_5", "password": "password5", "is_activated": 1},
    {"login": "user_6", "password": "password6", "is_activated": 0},
    {"login": "user_7", "password": "password7", "is_activated": 1},
    {"login": "user_8", "password": "password8", "is_activated": 0},
    {"login": "user_9", "password": "password9", "is_activated": 1},
    {"login": "user_10", "password": "password10", "is_activated": 0},
    {"login": "user_11", "password": "password11", "is_activated": 1},
]


# O(1)
def auth_user1(db, u):
    user = db.get(u["login"])  # O(1)
    if user is None:
        return "invalid user"
    elif user["password"] == u["password"] and user["is_activated"] == 0:  # O(1)
        return "need activation"
    elif user["password"] == u["password"] and user["is_activated"] == 1:  # O(1)
        return "authorized"
    else:
        return "invalid password"


# O(N)
def auth_user2(db, u):
    for user in db:  # O(N)
        if u["login"] == user.get("login") and u["password"] == user.get("password") and user.get(
                "is_activated") == 1:  # O(1)
            return "authorized"
        elif u["login"] == user.get("login") and u["password"] == user.get("password") and user.get(
                "is_activated") == 0:  # O(1)
            return "need activation"
        elif u["login"] == user.get("login") and u["password"] != user.get("password"):  # O(1)
            return "invalid password"
    return "invalid user"


user_for_check = {"login": "user_9", "password": "password9"}
print(auth_user1(DATABASE1, user_for_check))
print(auth_user2(DATABASE2, user_for_check))
