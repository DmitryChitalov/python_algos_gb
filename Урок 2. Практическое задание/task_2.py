"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
# user_numb = input("Enter number: ")
# user_numb = int(user_numb)
# ven_num, odd_num = 0, 0

# while user_numb > 1:

# 	last_numb = user_numb % 10
# 	user_numb //= 10
#
# 	if last_numb % 2 == 0:
# 		even_num += 1
# 	else:
# 		odd_num += 1
# print(f"Your number have '{even_num}' even elements and '{odd_num}' odd elements")


def rec_method(numb, even=0, odd=0):

	if numb == 0:  # базовое значение
		return even, odd  # возврат значений щетчика если условие верно

	else:
		last_n = numb % 10  # берем последний элемент числа
		numb = numb // 10  # удаляем из числа последний элемент
		if last_n % 2 == 0:  # проверка взятого элемента( четный или не четный)
			even += 1
			return rec_method(numb, even, odd)
		else:
			odd += 1
			return rec_method(numb, even, odd)


print(rec_method(123))
print(f"Your number have '{rec_method(123)[0]}' even elements and '{rec_method(123)[1]}' odd elements")