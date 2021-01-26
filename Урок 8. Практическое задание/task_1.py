"""Хаффман через коллекции"""


from collections import Counter

# Небольшое изменение - использован список вместо дека


def haffman_tree(s):
    count = Counter(s)
    sorted_elements = (sorted(count.items(), key=lambda item: item[1]))
    print(sorted_elements)
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements[0][0],
                    1: sorted_elements[1][0]}
            del sorted_elements[0]
            del sorted_elements[0]

            for j, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(j, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
                print(sorted_elements)

    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


# строка для кодирования
s = "beep boop beer!"


print(haffman_code(haffman_tree(s)))

for i in s:
    print(code_table[i], end=' ')
print()



