import pandas as pd
import numpy as np

tables = pd.read_html("https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C")
table = tables[12]
print(f"Прочитати за допомогою read_html: \n", table)
# print(f"Перші рядки таблиці метод head(): \n", table.head())
# print(f"Визначення рядків і стовпців: \n", table.shape)
# print(f"Заміна значень: \n", table.replace('--', None))
# print(f"Визначення значення всіх стовбців: \n", table.dtypes)
# print(f"Замініть типи не числових колонок на числові: \n", table[["2014", "2019"]] = table[["2014", "2019"]].apply(pd.to_numeric)
# print(f"яка частка пропусків міститься в кожній колонці \
#       (використовуйте методи isnull і sum): \n",
#       table.isnull().sum())
# print(f"Видаліть із таблиці дані по всій країні: \n",
#       table=table[:-1])

# print(f"Замініть відсутні дані в стовпцях середніми значеннями fillna: \n"
#       table=table.fillna({"1950": table["1950"].mean(), \
#                         "1960": table["1960"].mean(), \
#                         "1970": table["1970"].mean(),\
#                          "2014": table["2014"].mean(), \
#                         "2019": table["2019"].mean()}))
# print("""Отримайте список регіонів, 
# де рівень народжуваності 2019 року
#  був вищим за середній: \n""",
#       table[table["2019"] > table["2019"].mean()]["Регіон"])


# print(" найвища народжуваність ",
#       table[table["2014"] == table["2014"].max()])

# print("стовпчикова діаграму народжуваності \
# за регіонами у ---- році: \n",
#       table["2019"].plot(kind="bar"))
