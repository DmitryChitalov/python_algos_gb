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

import heapq
from collections import Counter, namedtuple

class Branches(namedtuple("Branches", ["left", "right"])):

  def walk(self,code,acc):
    self.left.walk(code, acc + '0')# пойти в левую ветвь, добавив к префиксу "0"
    self.right.walk(code, acc + '1')# пойти в правую ветвь, добавив к префиксу "1"

class Leaves(namedtuple("Leaves", ["char"])):

  def walk(self, code, acc):
    code[self.char] = acc or "0" # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"

def haffman_encode(s):
  my_lst = []
  for ch, weight in Counter(s).items():
    my_lst.append((weight, len(my_lst), Leaves(ch)))
  heapq.heapify(my_lst)
  count = len(my_lst)
  while len(my_lst) > 1:
    weight_1, count_1, left = heapq.heappop(my_lst)
    weight_2, count_2, right = heapq.heappop(my_lst)

    heapq.heappush(my_lst,(weight_1 + weight_2, count, Branches(left, right)))
    count += 1
  
  """
  [(15, 12, Branches(left=Branches(left=Leaves(char='b'), right=Leaves(char='e')), right=Branches(left=Branches(left=Leaves(char='p'), right=Leaves(char=' ')), right=Branches(left=Leaves(char='o'), right=Branches(left=Leaves(char='r'), right=Leaves(char='!'))))))]
  """
  code = {}
  if my_lst:
    [(_weight, _count, root)] = my_lst
    root.walk(code, '')
  
  return code

s = input('Введите строку: ')
code = haffman_encode(s)
encoded = ' '.join(code[ch] for ch in s)
print(encoded)
