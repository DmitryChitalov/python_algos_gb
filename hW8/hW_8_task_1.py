from collections import Counter, deque

str_for_code = "beep boop beer!"
code_table = dict()


class HaffCoder:

    def __init__(self, my_str):
        self.my_str = my_str
        self.n_simb = Counter(my_str)
        self.s_simb = deque(sorted(self.n_simb.items(), key=lambda value: value[1]))
        self.code_table = dict()

    def create_tree(self):
        if len(self.s_simb) != 1:
            while len(self.s_simb) > 1:
                bin_sum = self.s_simb[0][1] + self.s_simb[1][1]
                comb = {0: self.s_simb.popleft()[0],
                        1: self.s_simb.popleft()[0]}

                for i, _count in enumerate(self.s_simb):
                    if bin_sum > _count[1]:
                        continue
                    else:
                        self.s_simb.insert(i, (comb, bin_sum))
                        break
                else:
                    self.s_simb.append((comb, bin_sum))
        else:
            bin_sum = self.s_simb[0][1]
            comb = {0: self.s_simb.popleft()[0], 1: None}
            self.s_simb.append((comb, bin_sum))
        return self.s_simb[0][0]

    def haffman_code(tree, path =''):
        if not isinstance(tree, dict):
            code_table[tree] = path
        else:
            HaffCoder.haffman_code(tree[0], path=f'{path}0')
            HaffCoder.haffman_code(tree[1], path=f'{path}1')
        return code_table

    def print_code(self):
        code_list = []
        for i in self.my_str:
            code_list.append(code_table[i])
            print(code_table[i], end=' ')



my_str = HaffCoder(str_for_code)
my_tree = HaffCoder.create_tree(my_str)
HaffCoder.haffman_code(my_tree)
HaffCoder.print_code(my_str)