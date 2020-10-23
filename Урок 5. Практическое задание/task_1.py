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
from collections import namedtuple

## variables section
next_inter = True
incom_list = []
Company_tbl = []
incom_sum = 0
annual_incom = 0
avg_annual_incom = 0
rich_company = []
poor_company = []

# Шаблон
Company = namedtuple('Company', 'company_name q1 q2 q3 q4 summ')

if __name__ == "__main__":
    while next_inter:
        company_counter = int(input("Введите количество предприятий для расчета прибыли: "))
        if company_counter > 0:
            for i in range(company_counter):
                enterprise_name = input("Введите название предприятия: ")
                if enterprise_name != None:
                    enterprise_income = input("через пробел введите прибыль данного предприятия\n"
                                              "за каждый квартал(Всего 4 квартала): ")

                    for element in (enterprise_income.split(" ")):
                        if element.isdigit():
                            incom_list.append(int(element))
                        else:
                            incom_list.append(0)
                            print(f"The value must be a number: {element}")

                Company_tbl.append(Company(
                    company_name=enterprise_name,
                    q2=int(incom_list[0]),
                    q1=int(incom_list[1]),
                    q3=int(incom_list[2]),
                    q4=int(incom_list[3]),
                    summ=(int(incom_list[0])+int(incom_list[1])+int(incom_list[2])+int(incom_list[3]))
                ))
                incom_list.clear()

            for indx in range(len(Company_tbl)):
                print(f"Company {Company_tbl[indx].company_name} has annual incom ${Company_tbl[indx].summ}")
                annual_incom += Company_tbl[indx].summ

            print("- " * 50)
            avg_annual_incom = round((annual_incom / len(Company_tbl)),2)
            print("Средняя годовая прибыль всех предприятий: ${}".format(avg_annual_incom))

            for indx in range(len(Company_tbl)):
                if Company_tbl[indx].summ > avg_annual_incom:
                    rich_company.append(Company_tbl[indx].company_name)
                else:
                    poor_company.append(Company_tbl[indx].company_name)

            print("Предприятия, с прибылью выше среднего значения: {}".format(rich_company))
            print("Предприятия, с прибылью ниже среднего значения: {}".format(poor_company))

            print("- " * 50)

        while True:
            next_add = input("Хотите добавить дополнительное предприятие? (Да / Нет): ")
            if next_add.lower() in ('да', 'нет', 'yes', 'no', 'y', 'n'):
                next_inter = next_add.lower() in ('да', 'yes', 'y')
                rich_company.clear()
                poor_company.clear()
                annual_incom = 0
                break
            else:
                print("Ошибка ввода: введите ответ еще раз")

    print("- " * 50)


