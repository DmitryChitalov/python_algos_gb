"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""


class Lite_1c:
    from collections import defaultdict
    __company = defaultdict(float)

    def set_company(self):
        companus_count = int(input("Введите количество предприятий для расчета прибыли: "))
        while companus_count != 0:
            company_name = input("Введите название предприятия:")
            surce_data = input(
                "через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ")
            surce_data = surce_data.split()
            self.__company[company_name] = float(surce_data[0]) + float(surce_data[1]) + float(surce_data[2]) + float(
                surce_data[3])
            companus_count -= 1

    def annual_profi(self):
        company_count = len(self.__company)
        profit_awg = 0.0
        list_up_profit = []
        list_down_profit = []
        for company, sum in self.__company.items():
            profit_awg += sum
        print(f"Средняя годовая прибыль всех предприятий: {profit_awg / company_count}")
        for company, profit_company in self.__company.items():
            if profit_company > (profit_awg / 2):
                list_up_profit.append(company)
            else:
                list_down_profit.append(company)
        print(f"Предприятия, с прибылью выше среднего значения: {list_up_profit}")
        print(f"Предприятия, с прибылью ниже среднего значения: {list_down_profit}")


companys = Lite_1c()
companys.set_company()
companys.annual_profi()
