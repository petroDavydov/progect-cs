import pandas as pd
import numpy as np


read_file = pd.read_csv("2017_jun_final.csv")
# print(f"Simply read.csv: \n", read_file)
# print(f"Read with method head: \n", read_file.head())
# print(f"Read file use method shape: \n", read_file.shape)
# print(f"Use dtypes, for type of columns: \n", read_file.dtypes)
# print(f"Use isnull & sum: \n", read_file.isnull().sum())
# ---
# print(f"Delete use drop: \n", read_file.drop(
#     ['Должность', 'Специализация', 'Общий.опыт.работы',
#         'exp', 'salary', 'Валюта', 'cls'],
#     axis=1, inplace=True))
# print(f"Print after deleted using drop: \n", read_file.isnull().sum())
# print(f"Delete all raw use dropna: \n", read_file.dropna(inplace=True))
# print(f"Use shape onece more: \n", read_file.shape)
# ---

python_data = read_file[read_file['Язык.программирования'] == "Python"]
print(f"New python_data: \n", python_data)
print(f"New shape of table: \n ", python_data.shape)
print(f"Python Data use head(): \n ", python_data.head())
print(f"Use dtypes for new table python_data: \n", python_data.dtypes)
# ---
positions = python_data.groupby('Должность')
print(f"Use groupby: \n", positions)
# ---
data_position = positions['Зарплата.в.месяц'].agg(['min', 'max'])
print(f"Make new DataFrame, use agg: \n", data_position)
# -------------------------------


def fill_avg_sallary(raw):
    return (raw['min'] + raw['max']/2)


data_position['avg'] = data_position.apply(fill_avg_sallary, axis=1)
print(f"Use apply, custom function & make new column: \n", data_position)


print(f"Make statistics: \n", data_position['avg'].describe())

# data_position.to_csv("new_test_file.csv")

test = pd.read_csv('new_test_file.csv')
print(f"Read new_test_file.csv: \n", test)
