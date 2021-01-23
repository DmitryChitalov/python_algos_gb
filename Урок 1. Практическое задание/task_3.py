from collections import Counter

company_dict = {'company_1': 589632147,           # O(1)
                'company_2': 654789,
                'company_3': 789654123698,
                'company_4': 741258,
                'company_5': 32145696587412,
                'company_6': 963258741123}

count = Counter(company_dict)                    # O(1)
print(count.most_common(3))
