"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from sys import getrefcount


"""Первый урок 5ая задача."""

print(getrefcount(37))


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




"""Решение задачи 5 урока 2"""


def ascii_print(result_str: str, ascii_key: int, size: int):

    if size == 0 or ascii_key > 127:
        return result_str

    result_str += str(ascii_key) + " - " + chr(ascii_key) + " "

    return ascii_print(result_str, ascii_key + 1, size - 1)


length = 10
output = ""

for i in range(0, length):
    a_key = 32 + length*i
    output += ascii_print("", a_key, length) + "\n"

print(output)

