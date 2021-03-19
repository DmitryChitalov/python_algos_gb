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

from random import choice, randint

def gen_login(maxlen=8):
    SONANTS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    i1 = randint(0,1)
    i2 = randint(i1+1,maxlen)
    result = []
    for i in range(i1, i2+1):
        arr = SONANTS if i%2==0 else CONSONANTS
        result.append(choice(arr))
    return "".join(result)

def gen_passwd(n=5):
    return "".join(chr(randint(33,126)) for _ in range(n))

def gen_db(size=10):
    return {
        gen_login():[
            gen_passwd(),
            bool(randint(0,1))
        ]
        for i in range(size)
    }

STATUS_OK = 0
STATUS_INVALID_LOGIN = -1
STATUS_INVALID_PASSWD = -2
STATUS_NOT_ACTIVATED = -3

MESSAGES = {
    STATUS_OK: "Вход произведен успешно",
    STATUS_INVALID_LOGIN: "Неправильный логин",
    STATUS_INVALID_PASSWD: "Неправильный пароль",
    STATUS_NOT_ACTIVATED: "Учетная запись не активирована"
}

# Имеет смысл оценивать только время поиска

# Метод №1
def find_1(login):             # O(1)
    return db.get(login, [])   # O(1)

# Метод №2
def find_n(login):             # O(n)
    for k, v in db.items():      # O(n)
        if k == login:
            return v
    return []
# Очевидно, что метод №1 всегда быстрее, чем метод №2



def get_status(login, passwd, find=find_1):
    user = find(login)
    if not user:
        return STATUS_INVALID_LOGIN
    if user[0] != passwd:
        return STATUS_INVALID_PASSWD
    return STATUS_OK if user[1] else STATUS_NOT_ACTIVATED

def report(status):
    print(MESSAGES[status])



db = gen_db()
users = list(db.items())
print(users)

log1, pass1 = next((l,p) for l,(p,a) in users if a)
print(f"User: {log1}, password: {pass1}, active")

log2, pass2 = next((l,p) for l,(p,a) in users if not a)
print(f"User: {log1}, password: {pass1}, inactive")

print("Метод 1")
report(get_status("aaa", "bbb"))
report(get_status(log1, "bbb"))
report(get_status(log1, pass1))

report(get_status("aaa", "bbb"))
report(get_status(log2, "bbb"))
report(get_status(log2, pass2))

print("Метод 1")
report(get_status("aaa", "bbb", find_n))
report(get_status(log1, "bbb", find_n))
report(get_status(log1, pass1, find_n))

report(get_status("aaa", "bbb", find_n))
report(get_status(log2, "bbb", find_n))
report(get_status(log2, pass2, find_n))
