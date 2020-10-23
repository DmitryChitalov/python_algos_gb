"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
print("calculator")


# exit_flag = False
# while not exit_flag:
#	num1 = input("Enter first num: ")
#	num1 = int(num1)

#	act = input("Enter action: ")

#	num2 = input("Enter second num: ")
#	num2 = int(num2)

#	if act == '+':
#		print(f'{num1} + {num2} = {num1 + num2}')
#	elif act == '-':
#		print(f'{num1} - {num2} = {num1 - num2}')
#	elif act == '*':
#		print(f'{num1} * {num2} = {num1 * num2}')
#	elif act == '/':
#		zero_error = f'{num1} / {num2} = {num1 / num2}' if num1 != 0 and num2 != 0 else 'Zero divide zerro!!'
#		print(zero_error)

#	print('Хотите продолжить?')
#	ans = input('y/n: ')
#	if ans == 'n':
#		exit_flag = True
#	elif ans == 'y':
#		print('Продолжим...')
#	else:
#		print('не верный ввод, ещё раз..')
#		pass


def rec_calc():
	act = input("Enter action(+,-,*,/) or '0' to exit: ")
	if act == '0':
		return "Exit"
	else:
		try:

			num1 = input("first num: ")
			num2 = input("second num: ")
			num1, num2 = int(num1), int(num2)

			if act == '+':
				print(f'{num1} + {num2} = {num1 + num2}')
				return rec_calc()
			elif act == '-':
				print(f'{num1} - {num2} = {num1 - num2}')
				return rec_calc()
			elif act == '*':
				print(f'{num1} * {num2} = {num1 * num2}')
				return rec_calc()
			elif act == '/':
				zero_error = f'{num1} / {num2} = {num1 / num2}' if num1 != 0 and num2 != 0 else 'Error, divide by zero!!'
				print(zero_error)
				return rec_calc()
		except ValueError:
			print("Wrong input! try again!!")
			return rec_calc()


rec_calc()