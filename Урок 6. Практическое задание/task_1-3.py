from pympler import asizeof

class PageClass:
    def __init__(self, i_url, i_hash, i_salt):
        self.url  = i_url
        self.hash = i_hash
        self.salt = i_salt

class PageClassSlots:
    __slots__ = ('url', 'hash', 'salt')
    def __init__(self, i_url, i_hash, i_salt):
        self.url  = i_url
        self.hash = i_hash
        self.salt = i_salt

g_pc = PageClass('url_1', '12345678901234567890', 'qwertyuiop')
g_ss = PageClassSlots('url_2', '22345678901234567890', '2wertyuiop')
#print(g_pc.url, g_pc.hash, g_pc.salt)
#print(g_ss.url, g_ss.hash, g_ss.salt)
print(asizeof.asizeof((g_pc)))
print(asizeof.asizeof((g_ss)))
# Задача из урока 3, task 4: сохранение страниц в кэше.
# Страницы хранятся в виде объектов класса PageClass.
# Но если атрибуты класса хранить в виде слотов,
# а не в словаре, то объем объекта становится меньше,
# что и показывает функция asizeof.
# Причем длина самих атрибутов такая же.
# PageClass - класс, с хранением атрибутов в словаре.
# PageClassSlots - класс, с хранением атрибутов в слотах.
# Вывод данной задачи:
# 512
# 248
# Разрядность ОС: 64, python версии 3.9.0.

