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

# Решение 1
# Хранилище - словарь: {user : (password, is_activated), ...}
# Алгоритм - доступ к информации по ключу (user)
# Сложность - O(1) (без учета генерации словаря, c генерацией - O(n))

users = dict(user1=("password1", False), user2=("password2", True), user3=("password3", False),
             user4=("password4", True), user5=("password5", False))


def login_via_dict(user_id, password):
    """

    :param user_id:
    :param password:
    :return:   False - отказ в досутпе, True - доступ разрешен

    """
    user_data = users.get(user_id)
    if user_data is None:
        print(f"User '{user_id}' not found!")
        return False
    user_password, is_activated = user_data
    if password != user_password:
        print("Incorrect password!")
        return False
    if not is_activated:
        print(f"User '{user_id}' is not activated. Activate now? Y/N")
        answer = input()
        if answer and answer[0].upper() == 'Y':  # activation
            is_activated = True
            users[user_id] = (user_password, is_activated)
        else:
            print("Pls activate later and come back!")
            return False
    print("Login accepted")
    return True


login_via_dict("user1", "password1")

# Решение 2
# Хранилище - список кортежей: [(user, password, is_activated),...]
# Алгоритм - поиск перебором
# Сложность - O(n)

users = [("user1", "password1", False), ("user2", "password2", True), ("user3", "password3", False),
         ("user4", "password4", True), ("user5", "password5", False)]


def login_via_list(user_id, password):
    for id, user_data in enumerate(users):
        if user_data[0] == user_id:  # пользователь найден
            if user_data[1] == password:  # пароль верный
                if user_data[2] == False:  # учетка неактивирована
                    # предложить активацию
                    print(f"User '{user_id}' is not activated. Activate now? Y/N")
                    answer = input()
                    if answer and answer[0].upper() == 'Y':  # activation
                        users[id] = (user_id, password, True)
                    else:  # учетка неактивирована, выход
                        print("Pls activate later and come back!")
                        return False
                print("Login accepted")
                return True
            else:  # пароль неверный
                print("Incorrect password!")
                return False
    print(f"User '{user_id}' not found!")
    return False


login_via_list("user1", "password1")

# Вывод:
# Решение 1 эффективнее с точки зрения производительности на больших данных. O(1) лучше чем O(n)
