"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

    def push(self, elem):
        self.elems.insert(0,elem)

    def pop(self):
        if len(self.elems)==0: return
        return self.elems.pop(len(self.elems)-1)

def process_board():
    q_main = QueueClass()
    q_processed = QueueClass()
    q_repeat = QueueClass()

    v_cont = 'Y'
    while v_cont.upper()=='Y':
        print('Main queue:' + str(q_main.elems))
        print('Processed queue:' + str(q_processed.elems))
        print('Repeat queue:' + str(q_repeat.elems))

        print('Do you want to:')
        print('1 - insert new task')
        print('2 - process current task from main queue')
        print('3 - move current task from main queue to repeat queue')
        print('4 - process current task from repeat queue')
        v_op = input()
        if v_op.upper()=='1':
            print('Enter task:')
            v_val = input()
            q_main.push(v_val)
        if v_op.upper() == '2':
            if q_main.is_empty():
                print('There is nothing to solve!')
            else:
                v_val = q_main.pop()
                print('Task ' + str(v_val) + ' from MAIN is solved.')
                q_processed.push(v_val)
        if v_op.upper() == '3':
            if q_main.is_empty():
                print('There is nothing to move!')
            else:
                v_val = q_main.pop()
                print('Task ' + str(v_val) + ' is moved to repeat queue.')
                q_repeat.push(v_val)
        if v_op.upper() == '4':
            if q_repeat.is_empty():
                print('There is nothing to solve!')
            else:
                v_val = q_repeat.pop()
                print('Task ' + str(v_val) + ' from REPEAT is solved.')
                q_processed.push(v_val)
        print('Continue?(Y/N)')
        v_cont=input()


if __name__ == '__main__':

    process_board()