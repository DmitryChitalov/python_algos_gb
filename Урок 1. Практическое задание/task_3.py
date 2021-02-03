"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


class company_info:
    def __init__(self, company_name, yearly_revenue):
        self.company_name = company_name
        self.yearly_revenue = yearly_revenue


company_info_list1 = [company_info('Компания 1', 100), company_info('Компания 2', 300), company_info('Компания 3', 200),
                      company_info('Компания 4', 500), company_info('Компания 5', 50), company_info('Компания 6', 1000)]

#  способ o(n*log(n)):
company_info_list1.sort(key=lambda x: x.yearly_revenue, reverse=True)
print(company_info_list1[0].yearly_revenue, company_info_list1[1].yearly_revenue, company_info_list1[2].yearly_revenue)


# способ o(n)
def search_max_revenue(company_info_list, ignore_element_index1=None, ignore_element_index2=None):
    if len(company_info_list) < 2:
        raise Exception('Количество элементов в списке меньше двух.')
    current_maximum_index = next(iter(({0, 1, 2} - {ignore_element_index1, ignore_element_index2})))
    current_maximum = company_info_list[current_maximum_index].yearly_revenue
    for current_company_info_index in range(len(company_info_list)):
        if current_company_info_index == ignore_element_index1 \
                or current_company_info_index == ignore_element_index2:
            continue
        current_revenue = company_info_list[current_company_info_index].yearly_revenue
        if current_revenue > current_maximum:
            current_maximum = current_revenue
            current_maximum_index = current_company_info_index
    return current_maximum, current_maximum_index


max_revenue1, max_revenue1_index = search_max_revenue(company_info_list1)
max_revenue2, max_revenue2_index = search_max_revenue(company_info_list1, max_revenue1_index)
max_revenue3, max_revenue3_index = search_max_revenue(company_info_list1, max_revenue1_index, max_revenue2_index)
print(max_revenue1, max_revenue2, max_revenue3)
# Вывод - если оценивать скорось - лучше способ o(n) по причине
# более быстрого выполнения в случае большого кол-ва элементов
