"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import Counter, deque

x = Counter("Hello Harry!")
# x = Counter('beep boop beer!')

######################################
sorted_Counter = deque(sorted(x.items(), key=lambda el: el[1]))  # делаем отсортированый каунтер по возрастанию
# deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
# deque([('e', 1), ('o', 1), (' ', 1), ('a', 1), ('y', 1), ('!', 1), ('H', 2), ('l', 2), ('r', 2)])
# print(sorted_Counter)
if sorted_Counter != 1:
	while len(sorted_Counter) > 1:

		sumary_elem = sorted_Counter[0][1] + sorted_Counter[1][1]  # суммируем кол-во вхождений элементов

		node_tree = {0: sorted_Counter.popleft()[0],
		             1: sorted_Counter.popleft()[0]}  # удаляя элементы с дека создаем узел  где левый элемент имеет
		# значение(ключ) "0" а правый - "1"

		for i, _count in enumerate(sorted_Counter):  # что???
			# print(sumary_elem, ':', i, '--', _count)
			if sumary_elem >= _count[1]:  # если сумма вхождений элементов больше или равна
				# чем значение рядом стоящего элемента
				continue
			else:
				sorted_Counter.insert(i, (node_tree, sumary_elem))  # вставляем по текущему индексу
			# пару (ключ, значение)
				break
		else:
			sorted_Counter.append((node_tree, sumary_elem))

else:
	#
	sumary_elem = sorted_Counter[0][1]
	node_tree = {0: sorted_Counter.popleft()[0],
	             1: None}
	sorted_Counter.append((node_tree, sumary_elem))

# print('\t '*3, sorted_Counter[0][0])
lsd = sorted_Counter[0][0]
# {0: {0: 'b', 1: 'e'}, 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}}


binary_dict = dict()


def binary_convert(tree, path=''):
	if not isinstance(tree, dict):
		binary_dict[tree] = path

	else:
		binary_convert(tree[0], path=f'{path}0')
		binary_convert(tree[1], path=f'{path}1')


# --------------------------------------
t1 = Counter('beep boop beer!')
t = {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}  # уже готовое дерево по
# которому проходимся в поиске элементов
# --------------------------------------
binary_convert(t)
print(f'\nhardCode:    ', binary_dict)
for i in t1:
	print(binary_dict[i], end=' ')

##################################
print('\n')
##################################

binary_convert(lsd)
print(f'sorted list: ', binary_dict)
for i in x:
	print(binary_dict[i], end=' ')
print()
# 1 - 00 11 101 010 011 1000 1001 - готовый пример 'beep boop beer!'
# 3 - 00 01 100 101 110 1110 1111  - через обработку 'beep boop beer!'

# 2 - 100 1110 101 1111 000 001 110 010 011 - "Hello Harry!"




