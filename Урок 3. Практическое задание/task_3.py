"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:
apap

рар
ра
ар
ара
р
а
"""
import hashlib


def get_str_list(str_any, str_list_in=[], _counter=1):
    """
    функция получает строку и возвращяет список подстрок
    :param str_any: str
    :param str_list_in: list
    :param _counter: int
    :return: list
    """
    if len(str_any) == _counter:
        return str_list_in
    else:
        str_list_in.append(str_any[_counter:])
        str_list_in.append(str_any[:-_counter])
        _counter += 1
        return get_str_list(str_any, str_list_in, _counter)


def get_lst_str_all(list_s: list, an_str: str):
    """
    функция получает список подстрок и строку,
    возвращяет дополненный список
    :param list_s: list
    :param an_str: str
    :return: list
    """
    for elem in an_str[1:-1]:
        list_s.append(elem)
    counter = 0
    for _ in range(len(an_str)):
        counter += 1
        tmp_1 = an_str[counter:-counter]
        if tmp_1 == '':
            break
        list_s.append(tmp_1)
    return list_s


def create_hash(list_str_all_in: list) -> list:
    """
    функция получает список подстрок и возвращяет список хэшей
    :param list_str_all_in: list
    :return: list
    """
    res_list = map(lambda x: hashlib.sha3_256(x.encode('utf-8')).hexdigest(), list_str_all_in)
    return list(res_list)


def check_str(list_hash: list) -> bool:
    """
    функция получает список хэшей и проверяет их на уникальность
    возвращяет bool
    :param list_hash: list
    :return: bool
    """
    return len(list_hash) == len(set(list_hash))


def main(any_str):
    list_str = get_str_list(any_str)
    list_str_all = get_lst_str_all(list_str, any_str)
    print(list_str_all)
    print(check_str(create_hash(list_str_all)))


if __name__ == '__main__':
    # my_str = 'papa'
    # main(my_str) # False
    my_str_1 = 'Python'
    main(my_str_1)  # True
