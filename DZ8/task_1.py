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

class TreeNode:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_сhild(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


def two_minimal_numbers_array(array):
    first_min = second_min = None
    maximum = max(array)

    # Первое минимальное значение
    for index, number in enumerate(array):
        if number <= maximum:
            maximum = number
            first_min = (number, index)

    maximum = max(array)
    # Второе минимальное значение, пропуская первое найденное
    for index, number in enumerate(array):
        if index != first_min[1]:
            if number <= maximum:
                maximum = number
                second_min = (number, index)

    # Возвращаем кортеж вида ((m1, i1), (m2, i2)), где mn - n-ое минимальное значение, in - его индекс
    return first_min, second_min

def create_bin_codes(main_node, bin_codes, code):
    if main_node.has_left_сhild():
        # Идем влево - к символу добавляется 0
        code += "0"
        # Если левый ребенок - символ, то добавляем его и его код в bin_codes
        if isinstance(main_node.left_child, str):
            bin_codes[main_node.left_child] = code
            # Идем обратно - убираем последнюю цифру code
            code = code[:-1]
        # Если нет - рекурсивно вызываем функцию с новым main_node
        else:
            create_bin_codes(main_node.left_child, bin_codes, code)
            # Идем обратно - убираем последнюю цифру code
            code = code[:-1]
    if main_node.has_right_child():
        # Идем вправо - к символу добавляется 1
        code += "1"
        # Если правый ребенок - символ, то добавляем его и его код в bin_codes
        if isinstance(main_node.right_child, str):
            bin_codes[main_node.right_child] = code
            # Идем обратно - убираем последнюю цифру code
            code = code[:-1]
        # Если нет - рекурсивно вызываем функцию с новым main_node
        else:
            create_bin_codes(main_node.right_child, bin_codes, code)
            # Идем обратно - убираем последнюю цифру code
            code = code[:-1]

# Тестовая строка
source = "Hello world"
# Словарь частот
letters = {}
# Отдельный список с частотой каждого символа
frequency = []
# Он нужен, так как в дальнейшем в словаре будут появляться значения
# класса TreeNode, которые не могут сравниваться с числами

# Заполнение словаря частот
for i in source:
    if not letters.get(i):
        letters[i] = 0
    letters[i] = letters[i] + 1

# Заполнение списка частот
for i in letters:
    frequency.append(letters[i])

# Проходимся по списку, оставляя в итоге 1 элемент
for i in range(len(letters)-1):
    # Возвращает кортеж вида ((m1, i1), (m2, i2)), где mn - n-ое минимальное значение, in - его индекс
    minimals = two_minimal_numbers_array(frequency)

    # Ключ первого минимального значения
    key_first = list(letters.keys())[minimals[0][1]]
    # Ключ второго минимального значения
    key_second = list(letters.keys())[minimals[1][1]]
    # Для того, чтобы вставлять в value каждого TreeNode
    node_key = key_first + key_second

    # Удаляем старые значения
    frequency.remove(minimals[0][0])
    frequency.remove(minimals[1][0])
    # Складываем значения и вставляем их на последнее место
    frequency.append(minimals[0][0] + minimals[1][0])

    # Здесь выполняется проверка, чтобы в потомках TreeNode записывались не сами строки,
    # длина которых > 1, а узлы, у которых value = этим строкам
    if len(key_first) > 1 and len(key_second) > 1:
       letters[node_key] = TreeNode(0, node_key, letters[key_first], letters[key_second])
    elif len(key_first) > 1:
       letters[node_key] = TreeNode(0, node_key, letters[key_first], key_second)
    elif len(key_second) > 1:
       letters[node_key] = TreeNode(0, node_key, key_first, letters[key_second])
    else:
       letters[node_key] = TreeNode(0, node_key, key_first, key_second)

    # Удаляем использованные элементы
    letters.pop(key_first)
    letters.pop(key_second)

# Берем значение первого (и единственного) элемента
final_tree = letters[next(iter(letters))]

del frequency, letters

# bin_codes - словарь, который содержит бинарный код для каждого символа
bin_codes = {}
# Переменная, содержащая бинарный код, в зависимости от движения по дереву
code = ""

# Вызываем функцию обхода дерева с присвоением бинарного кода символам
create_bin_codes(final_tree, bin_codes, code)

del final_tree, code

# Кодирование строки
final_bin_string = ""
for letter in source:
    final_bin_string += (bin_codes[letter] + " ")
print(source)
print(bin_codes)
print(final_bin_string)