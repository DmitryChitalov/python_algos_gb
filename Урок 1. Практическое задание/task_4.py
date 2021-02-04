"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
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


users_list =[{"user": "Иванов", "pass": "Ivanov01", "active": True},
             {"user": "Петров", "pass": "Petrov01", "active": False},
             {"user": "Сидоров", "pass": "Sidorov01", "active": False},
             {"user": "Попов", "pass": "Popov01", "active": True},
             {"user": "Кравцов", "pass": "Kravtsov01", "active": False},
             {"user": "Иванов1", "pass": "Ivanov02", "active": True},
             {"user": "Илонова", "pass": "Ivanov02", "active": True},
             {"user": "Исмаилова", "pass": "Ivanov02", "active": True},
             {"user": "Иванова", "pass": "Ivanov02", "active": True},
             {"user": "Петров2", "pass": "Petrov02", "active": False},
             {"user": "Сидоров3", "pass": "Sidorov03", "active": False},
             {"user": "Попов2", "pass": "Popov02", "active": True},
             {"user": "Кравцов1", "pass": "Kravtsov02", "active": False}]
letter_user_dict = {}


def activation(user_dict):
    name = user_dict["user"]
    print(f"Пользователь {name}, активируйтесь пожалуйста! ")
    pass


def step_1(user_dict):
    name = user_dict["user"]
    print(f"Пользователь {name}, добро пожаловать!")
    pass


login = input("Логин: ")
password = input("Пароль: ")


users = {"Иванов": {"pass": "Ivanov01", "active": True},
         "Петров": {"pass": "Petrov01", "active": False},
         "Сидоров": {"pass": "Sidorov01", "active": False},
         "Попов": {"pass": "Popov01", "active": True},
         "Кравцов": {"pass": "Kravtsov01", "active": False},
         "Иванов1": {"pass": "Ivanov02", "active": True},
         "Илонова": {"pass": "Ivanov02", "active": True}}


# Данное решение дополняю после урока 3, на котором Вы упомянули, что логин всегда уникален.
# В этом случае можно иначе сформировать нашу базу ) В виде единного словаря, где ключом выступает имя.
# Тогда это наиболее оптимальное решение O(1)
def check_user_0(log, user_pass):
    print(users[log].get("pass"))
    if log in users.keys() and users[log].get("pass") == user_pass:
        if users[log].get("active"):
            print("Добро пожаловать!")
        else:
            print("Требуется активация!")
    else:
        print("Такого пользователя не существует!")


# или так, еще лучше! (меньше мусора в памяти):
users_l = {"Иванов": ["Ivanov01", True],
         "Петров": ["Petrov01", False],
         "Сидоров": ["Sidorov01", False],
         "Попов": ["Popov01", True]}


def check_user_01(log, user_pass):
    if log in users_l.keys() and users_l[log][0] == user_pass:
        if users_l[log][1]:
            print("Добро пожаловать!")
        else:
            print("Требуется активация!")
    else:
        print("Такого пользователя не существует!")


print("check_user_0()")
check_user_0(login, password)
print("check_user_01()")
check_user_01(login, password)


# решение 1 O(n) - пробегаем по всем элементам списка
def check_user_1(log, user_pass):
    for user_info in users_list:
        if login == user_info["user"] and password == user_info["pass"]:
            if user_info["active"]:
                step_1(user_info)
                break
            else:
                activation(user_info)
                break
    else:
        print("Пока такого пользователя не существует!")

# Второе решение, можно всех пользователей разложить по алфавиту,
# создать словарь списков по буквам. и искаить уже среди них
# O(n) - оценка данной функции.
# Но, если эта функция можно быть выполнена один раз, чтоб к ней постоянно не возращаться
# Например: вызываем ее один раз и записываем результат в какой-нибудь файл, а далее уже обращаемся
# к этому файлу. (В в рамках этой задачи, когда а пользователи могут постоянно добавляться и
# авторизоваться это сомнительный вариант.

abc: set = {}


# создаем {"letter1": [letter_user_lists{}, {}, {}], "Letter2": [{},{}], ...}
def abc_user_dict(i_users_list):
    u_list = i_users_list.copy()

    # для начала вытянем первые буквы всех пользователей:

    abc = {(user_info["user"][0].lower()) for user_info in u_list}

    print(abc)

    for letter in abc:
        temp_list = []
        for user_inf in u_list:
            if letter == (user_inf["user"][0]).lower():
                temp_list.append(user_inf)
                u_list.remove(user_inf)
        letter_user_dict[letter] = temp_list
    print(letter_user_dict)


# ЕСЛИ считать, что нам НЕ ТРЕБУЕТСЯ запускать каждый раз построение словаря с группировкой по буквам,
# то чисто данный метод - O(n) ~ n/количество букв. Т.е. тоже линейная, но более эффективная.
# в противном случае к этой оценке еще надо прибавить O(n) И тогда она проигрывает check_user_1.
def check_user_2(i_login, i_password):
    first_letter = i_login[0]
    letter_stack = {}
    print(first_letter)

    letter_stack = letter_user_dict.get(first_letter.lower())
    print(letter_stack)

    if letter_stack is None:
        print("Пока такого пользователя не существует.")
        exit()

    for user_info in letter_stack:
        if login == user_info["user"] and password == user_info["pass"]:
            if user_info["active"]:
                step_1(user_info)
                break
            else:
                activation(user_info)
                break
    else:
        print("Пока такого пользователя не существует!")

print("check_user_1()")
check_user_1(login, password)

# print("Cailling alghabet_user_dict:")
abc_user_dict(users_list)

print("check_user_2()")
check_user_2(login, password)
