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

users = {'vasya': ['123', 0], 'petya': ['123', 0], 'artem': ['123', 1]}


def web_access(dictionary):  # Сложность O(n)
	while True:
		message = input("Hello, if you want to log in, press 'y' or 'q' for exit: ")
		if message == 'q':
			return print('End of programm')
		else:
			login = input('Enter login: ')
			password = input('Enter password: ')
			if dictionary.get(login) != None:
				if dictionary[login][0] == password:
					if dictionary[login][1] == 1:
						return print('Access grant')
					else:
						print('Access denied, please activate account')
				else:
					print('Password incorrect, try again')
			else:
				print('Login incorrect, please try again')


def web_access2(dictionary): # Сложность O(n^2)
	while True:
		message = input("Hello, if you want to log in, press 'y' or 'q' for exit: ")
		if message == 'q':
			return print('End of programm')
		else:
			login = input('Enter login: ')
			password = input('Enter password: ')
			error_pass = 0
			error_login = 0
			for key in dictionary.keys():
				if login == key:
					if dictionary[login][0] == password:
						if dictionary[login][1] == 1:
							return print('Access grant')
						else:
							return print('Access denied, please activate account')
					else:
						error_pass += 1
				else:
					error_login +=1
			if error_login > len(dictionary):
				print('Login incorrect, please try again')
			elif error_pass > 0:
				print('Password incorrect, try again')
			elif error_login > len(dictionary) and error_pass > 0:
				print('Login and password incorrect')
				
			


web_access2(users)
web_access(users)
# Эффективнее использовать функцию web_access т.к. она имееет линейную сложность. Функция web_access2 имеет квадратичную сложность за счет использования вложенных циклов
