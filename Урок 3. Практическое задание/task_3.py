"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
from uuid import uuid4
import hashlib
str_data = "papa_roach"
data_set = set()
salt = uuid4().hex


def count_str(str_input):
    if len(str_input) == 0:
        print(f"Хеш с итоговыми подстроками - {data_set}")
        print(f"Количество подстрок в строке - {len(data_set)}")
        return
    if str_input != str_data:
        res = hashlib.sha256(salt.encode() + str_input.encode()).hexdigest()
        data_set.add(res)
    for i in range(1, len(str_input)):
        res = hashlib.sha256(salt.encode() + str_input[:-i].encode()).hexdigest()
        data_set.add(res)
    count_str(str_input[+1:])


count_str(str_data)

