# Задача на бинарные деревья, игра "Животные".
# Пример работы программы:
# ---
# Оно живет в воде? n
# Оно имеет больше трех ног? n
# Это человек? n
# Кто это? орел
# Чем орел отличается от человек? имеет крылья
# Благодарю за информацию! Продолжим? y
# Оно живет в воде? n
# Оно имеет больше трех ног? n
# Оно имеет крылья? y
# Это орел? y
# Я угадал! Ура!!!
# Продолжим? n
# ---

import yaml

KNOWLEDGE = """
Q: живет в воде
Y:
  Q: имеет щупальца
  Y:
    Q: имеет больше девяти щупалец
    Y: кальмар
    N: осьминог
  N:
    Q: дышит воздухом
    Y:
      Q: имеет спинной плавник
      Y: дельфин
      N: кит
    N: рыба
N:
  Q: имеет больше трех ног
  Y:
    Q: имеет копыта
    Y: лошадь
    N: собака
  N: человек
"""


class BinaryTree:
    @classmethod
    def fromYAML(cls, yamlstr):
        return cls.fromdict(yaml.safe_load(yamlstr))

    @classmethod
    def fromdict(cls, thedict):
        if not isinstance(thedict, dict):
            return cls(thedict)
        left = cls.fromdict(thedict["Y"])
        right = cls.fromdict(thedict["N"])
        val = thedict["Q"]
        return cls(val, left, right)

    def __init__(self, root_obj, left=None, right=None):
        self.root = root_obj
        self.left_child = left
        self.right_child = right

    def __str__(self):
        return f'({self.left_child}, {self.root}, {self.right_child})'

    def has_children(self):
        return self.right_child is not None or self.left_child is not None

    def toYAML(self):
        return yaml.dump(self.todict(), allow_unicode=True)

    def todict(self):
        if not self.has_children():
            return self.root
        left = (
            self.left_child.todict()
            if isinstance(self.left_child, BinaryTree)
            else self.left_child)
        right = (
            self.right_child.todict()
            if isinstance(self.right_child, BinaryTree)
            else self.right_child)
        return {'Q': self.root, 'Y': left, 'N': right}

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def create_right_child(self, val):
        self.right_child = BinaryTree(val)

    def create_left_child(self, val):
        self.left_child = BinaryTree(val)

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


# если пользователь вместо ввода пишет exit
class ExitCommand(Exception):
    pass


# Для ответа да/нет с возможностью выхода из программы
def mybool(inp):
    inp = inp.lower()
    if inp in ('q', 'quit', 'e', 'exit', 'в', 'выход'):
        raise ExitCommand()
    if inp in ('n', 'no', '0', 'н', 'нет', '-'):
        return False
    return True


# Угадывание животного сводится к спуску по бинарному дереву
def loop():
    # бинарное дерево == база знаний
    root = BinaryTree.fromYAML(KNOWLEDGE)
    # текуций узел
    cursor = root
    while True:
        try:
            childnode = (
                cursor.get_left_child()
                if mybool(input(f'Оно {cursor.get_root_val()}? '))
                else cursor.get_right_child())
            if childnode.has_children():
                cursor = childnode
                continue
            else:
                child = childnode.get_root_val()
                if mybool(input(f'Это {child}? ')):
                    print('Я угадал! Ура!!!')
                    if mybool(input(f'Продолжим? ')):
                        cursor = root
                        continue
                    else:
                        break
                else:
                    who = input('Кто это? ')
                    question = input(f'Чем {who} отличается от {child}? ')
                    childnode.set_root_val(question)
                    childnode.create_left_child(who)
                    childnode.create_right_child(child)
                    if mybool(input(f'Благодарю за информацию! Продолжим? ')):
                        cursor = root
                        continue
                    else:
                        break
        except ExitCommand:
            break


if __name__ == "__main__":
    loop()
