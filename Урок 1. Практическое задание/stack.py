class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        n = 0
        self.elems.append([])
        for i in range(1, el):
            if len(self.elems[n]) // 5 == 0:
                self.elems[n].append(i)
            else:
                self.elems.append([])
                n += 1
                self.elems[n].append(i)




    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def get_elems(self):
        return self.elems


if __name__ == '__main__':

    SC_OBJ = StackClass()

    SC_OBJ.push_in(21)

    print(SC_OBJ.stack_size())

    print(SC_OBJ.get_elems())
