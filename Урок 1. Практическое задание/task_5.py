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
class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, el):
        self.elems.append(el)

    def pop(self):
        return self.elems.pop()

    def get_size(self):
        return len(self.elems)

class StackOfStacksClass:
    def __init__(self):
        self.stacks = []
        self.cur_stack=-1
        self.max_stack_size=3

    def is_emptys(self):
        return self.elems == []

    def pushs(self, el):
        if(self.stacks==[] or self.cur_stack==-1 or self.stacks[self.cur_stack].get_size==self.max_stack_size):
            new_stack=StackClass()
            self.stacks.append(new_stack)
            self.cur_stack = self.cur_stack + 1
        (self.stacks[self.cur_stack]).push(el)

    def pops(self):
        if (self.stacks == []):return
        if (self.cur_stack<0): return
        v_ret=(self.stacks[self.cur_stack]).pop()
        if (self.stacks[self.cur_stack].get_size()==0 and self.cur_stack>0):
            self.stacks.remove(self.cur_stack)
            self.cur_stack=self.cur_stack-1
        return v_ret

    def get_sizes(self):
        if len(self.stacks)==0:
            return 0
        else:
            return self.max_stack_size*self.cur_stack+(self.stacks[self.cur_stack]).get_size()

def dishes():
    v_cont = 'Y'
    v_stacks = StackOfStacksClass()
    while v_cont.upper()=='Y':
        print('In or out?(I/O)')
        v_op = input()
        if v_op.upper()=='I':
            print('Enter value:')
            v_val = input()
            v_stacks.pushs(v_val)
        if v_op.upper() == 'O':
            v_val = v_stacks.pops()
            print('Out:' + str(v_val))
        print('Continue?(Y/N)')
        v_cont=input()

if __name__ == '__main__':

    dishes()
