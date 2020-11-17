"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
import random


class DashStack:
    def __init__(self, max_cnt_in_stack):
        self._max_cnt_in_stack = max_cnt_in_stack
        self.__items = [[]]

    def clear(self):
        self.__items.clear()

    def is_empty(self):
        return len(self.__items) == 0

    def add_substack(self):
        self.__items.append([])

    def push_back(self, el):
        if len(self.__items[-1]) == self._max_cnt_in_stack:
            self.add_substack()
        self.__items[-1].append(el)

    def pop_back(self):
        out = self.__items[-1].pop()
        if len(self.__items[-1]) == 0:
            self.__items.pop()
        return out

    def at(self, index):
        item_index = index - self._max_cnt_in_stack - 1  # start count from zero
        stack_index = self.length() // index
        stack = self.__items[stack_index]
        # print(f"stacks {len(self.__items)}")
        # print(f"goto stack {stack_index + 1}")  # pretty human print
        # print(f"index in stack {item_index + 1}")  # pretty human print
        return stack[item_index]

    def get_all(self):
        res = []
        for substack in self.__items:
            res += substack
        return res

    def length(self):
        all_except_lost_size = (len(self.__items) - 1) * self._max_cnt_in_stack
        lost_size = len(self.__items[-1])
        all_length = all_except_lost_size + lost_size
        return all_length


def main():
    test_stack = DashStack(5)
    for _ in range(10):
        test_stack.push_back(random.randint(1, 100))

    print(f"ful stack size: {test_stack.length()}")
    print(f"all items in stack {test_stack.all()}")
    print(f"item at 6 {test_stack.at(6)}")
    print(f"pop lost {test_stack.pop_back()}")
    print(f"ful stack size: {test_stack.length()}")
    print(f"all items in stack {test_stack.get_all()}")


if __name__ == "__main__":
    main()
