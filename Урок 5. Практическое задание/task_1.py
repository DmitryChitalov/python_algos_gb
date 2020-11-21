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


def ask_number(message):
    pass
    res = input(message).strip()
    if not res.isdigit():
        print("Недопустимый ввод! Разрешены к вводу только цифры!")
        return ask_number(message)

    return int(res)


def ask_company_name(message):
    res = input(message).strip()

    return res


def ask_company_profit(message):
    res = input(message).strip()

    if len(res.split()) < 4:
        res = ask_company_profit(message)

    return res.split()


def main():
    pass
    try:
        total_profit = {}
        below_average = []
        above_average = []
        companies = namedtuple("company", "q1 q2 q3 q4")
        company_counter = ask_number("Введите количество компаний ")

        for i in range(1, company_counter + 1):
            print(f"Ввод данных {i}-й компании")
            name = ask_company_name("Введите название компании ")
            all_quatter_profit = ask_company_profit("Введите прибыль за 4 квартала через пробел ")
            company = companies(q1=int(all_quatter_profit[0]), q2=int(all_quatter_profit[1]),
                                q3=int(all_quatter_profit[2]), q4=int(all_quatter_profit[3]))
            total_profit[name] = (company.q1 + company.q2 + company.q3 + company.q4) / len(all_quatter_profit)

        average_profit_all_companies = sum(total_profit.values()) / len(total_profit.values())
        print(f"Средняя прибыль всех компаний за 4 квартала - {average_profit_all_companies}")

        for key, value in total_profit.items():
            if value < average_profit_all_companies:
                below_average.append(key)
            else:
                above_average.append(key)

        print(f"Компаний с прибылью ниже среднего - {', '.join(below_average)}")
        print(f"Компаний с прибылью выше среднего - {', '.join(above_average)}")

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
