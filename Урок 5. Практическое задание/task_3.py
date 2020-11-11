"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit

test_list = []
test_deque = deque()


def list_test_append_right(cyclces):
    for i in range(cyclces):
        test_list.append(i)


def deque_test_append_right(cyclces):
    for i in range(cyclces):
        test_deque.append(i)


def list_test_pop_right(cyclces):
    for i in range(cyclces):
        test_list.pop()


def deque_test_pop_right(cyclces):
    for i in range(cyclces):
        test_deque.pop()


def list_test_append_left(cyclces):
    for i in range(cyclces):
        test_list.insert(0, i)


def deque_test_append_left(cyclces):
    for i in range(cyclces):
        test_deque.appendleft(i)


def list_test_pop_left(cyclces):
    for i in range(cyclces):
        test_list.pop(0)


def deque_test_pop_left(cyclces):
    for i in range(cyclces):
        test_deque.popleft()


def list_test_insert_middle(cyclces):
    for i in range(cyclces):
        test_list.insert(len(test_list) // 2, i)


def deque_test_insert_middle(cyclces):
    for i in range(cyclces):
        test_deque.insert(len(test_deque) // 2, i)


def list_test_delete_middle(cyclces):
    for i in range(cyclces):
        del test_list[len(test_list) // 2]


def deque_test_delete_middle(cyclces):
    for i in range(cyclces):
        del test_deque[len(test_deque) // 2]


funcs_list = {'append_right': 'list_test_append_right',
              'pop_right': 'list_test_pop_right',
              'append_left': 'list_test_append_left',
              'pop_left': 'list_test_pop_left',
              'insert_middle': 'list_test_insert_middle',
              'delete_middle': 'list_test_delete_middle'}

funcs_deque = {'append_right': 'deque_test_append_right',
               'pop_right': 'deque_test_pop_right',
               'append_left': 'deque_test_append_left',
               'pop_left': 'deque_test_pop_left',
               'insert_middle': 'deque_test_insert_middle',
               'delete_middle': 'deque_test_delete_middle'}

setup = f"""from __main__ import test_list, test_deque, {", ".join(funcs_list.values())}, {", ".join(funcs_deque.values())}"""

print(f'{"":>15}{"list":>15}{"deque":>15}')
for item in funcs_list:
    list_result = timeit(f'{funcs_list[item]}(500)', setup, number=500)
    deque_result = timeit(f'{funcs_deque[item]}(500)', setup, number=500)
    print(f'{item:>15}{list_result:>15.6f}{deque_result:>15.6f}')


"""
                          list          deque
   append_right       0.023497       0.017827
      pop_right       0.017262       0.016630
    append_left      12.842424       0.016644
       pop_left       6.887636       0.016595
  insert_middle       6.413091      15.025932
  delete_middle       3.359001      16.056544
  
  1. deque и list работают одинаково если дописывать и удалять элементы в конце коллекции
  2. если дописывать и удалять элементы в начале, то заметный выигрыш дает реализация deque
  3. В случае, если необходимо работать с элементами в середине списка, лучшим решением будет использование list
  
  Встав перед выбором что лучше использовать, нужно проанализировать какие операции будут происходить в коллекции в 
  контексте текущей задачи. И основываясь на перечисленных выше пунктах сделать выбор в пользу list или deque
"""