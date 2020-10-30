"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""


def simple(i):
	"""Без использования «Решета Эратосфена»"""
	count = 1
	n = 2
	while count <= i:
		t = 1
		is_simple = True
		while t <= n:
			if n % t == 0 and t != 1 and t != n:
				is_simple = False
				break
			t += 1
		if is_simple:
			if count == i:
				break
			count += 1
		n += 1
	return n


# i = int(input('Введите порядковый номер искомого простого числа: '))
i = 100
print(simple(i))

# ################################################################################


def eratosthenes(n):
	sieve = list(range(n + 1))
	sieve[1] = 0
	for i in sieve:
		if i > 1:
			for j in range(i + i, len(sieve), i):
				sieve[j] = 0

	return sieve


print(sum(eratosthenes(100)))


