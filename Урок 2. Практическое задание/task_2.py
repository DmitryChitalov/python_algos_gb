"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def check_number(number, chet=0, nechet=0):
	if number == 0:
		return f"Четные числа {chet}\nНе четные числа {nechet}" 
	else:
		if (number % 10) % 2 == 0:
			return check_number(number // 10, chet + 1, nechet)
		else:
			return check_number(number // 10, chet, nechet + 1)
		

print(check_number(34560))
