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
import itertools

# companies_list = []
# total_number = 0
#
# # заполняем списко словарей {name, profit}
#
# try:
#     total_number = int(input("Сколько компаний Вы желаете зарегистрировать? "))
#     if total_number <= 3:
#         print("Маловато будет... ")
#         exit()
#     for i in range(total_number):
#         name = input("Название компании: ")
#         profit = float(input(f"Годовая прибыль компании {name}: "))
#         companies_profit_dict = {"name": name, "profit": profit}
#
#         companies_list.append(companies_profit_dict)
# except ValueError:
#     print("Некорректный ввод")
#     exit()
#
# print(companies_list)


# решение с использованием встроенного метода sorted()
# O(n*log(n))
def high_yield_companies_1(comp_list):
    sorted_comp_list = sorted(comp_list, key=lambda k: k["profit"], reverse=True)  # O(n*log(n))
    print(sorted_comp_list[:3])  # O(1)


# Находим максимум в списке и переносим его в выходной список. Повторяем эту операцию 3 раза в цикле.
# O(n) - решение эффективнее! По приведенной оценке.
def high_yield_companies_2(comp_list):
    full_list = comp_list.copy()
    high_yield_list = []
    for count in range(3):
        # с помощью встроенной функции max:
        # temp_dict = max(comp_list, key=lambda k: k["profit"])
        # изобретаем велосипед:
        temp_dict = full_list[0]
        idx = 1

        while idx < len(full_list):
            if temp_dict["profit"] < full_list[idx]["profit"]:
                temp_dict = full_list[idx]
            idx += 1

        high_yield_list.append(temp_dict)
        full_list.remove(temp_dict)

    print(high_yield_list)


# Логика данного алоритма след: Берем 3 первых словаря из списка и дальше последовательно пробегаем по всему словарю
# и каждый последующий элемент сравниваем с этими элементами. Если его profit больше чем одно из них, то заменяем
# словарь
# O(n)
def high_yeild_companies_3(comp_list):
    high_yield_list = comp_list[:3]

    for idx_base, comp_dict in enumerate(comp_list[3:]):
        high_yield_list = sorted(high_yield_list, key=lambda k: k["profit"])  # O(3*log3) - const

        for idx_high, yield_dict in enumerate(high_yield_list[:]):
            if comp_dict["profit"] > yield_dict["profit"]:
                high_yield_list[idx_high] = comp_dict
                break

    print(high_yield_list)

    return high_yield_list

companies_list = [{'name': 'firm_1', 'profit': 234.0}, {'name': 'firm_2', 'profit': 76.0},
                  {'name': 'firm_3', 'profit': 35.0}, {'name': 'firm_4', 'profit': 765.0},
                  {'name': 'firm_5', 'profit': 453.0}, {'name': 'firm_6', 'profit': 132.0},
                  {'name': 'firm_7', 'profit': 654.0}]

high_yield_companies_1(companies_list)
high_yield_companies_2(companies_list)
high_yeild_companies_3(companies_list)