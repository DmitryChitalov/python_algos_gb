"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
import time
from binascii import hexlify

data_base = {}


def check_time(func):
	"""decorator"""

	def wraper(arg1, arg2):
		start_check = time.time()
		return_func = func(arg1, arg2)
		end_check = time.time()

		print(f"\nПроцесс обработки операции занял: {round(end_check - start_check, 4)} сек.\n")
		return return_func

	return wraper


# ########################################


@check_time
def hashing(pas, log):
	obj = hashlib.pbkdf2_hmac(hash_name='sha256',
	                          password=pas.encode('utf-8'),
	                          salt=log.encode('utf-8'),
	                          iterations=100000)
	res = hexlify(obj)
	data_base[log] = {'password': pas, 'hash': res}

	return res


user_login = input("Enter your Login: ")
user_pass = input("Enter your password: ")

print("В базе данных хранится строка: ", hashing(user_pass, user_login))
#######
print()
#######
user_check = input("Enter your password again: ")
if user_check:
	check_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
	                                password=user_check.encode('utf-8'),
	                                salt=user_login.encode('utf-8'),
	                                iterations=100000)
	res2 = hexlify(check_obj)
	if res2 == data_base[user_login]['hash']:
		print("Вы ввели правильный пароль")
	else:
		print("Пароль не верный, повторите попытку!")

