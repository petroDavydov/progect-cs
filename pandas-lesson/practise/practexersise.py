import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Maria', 'Petro', 'Sophia', 'Max', 'Natalia', 'Vadym'],
    'Вік': [21, 22, 20, 19, 23, 22, 21, 20, 19, 21],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics'],
    'Хобі': ['Jump', 'Read', 'Swim', 'Look', 'Eat', 'Work', 'Write', 'Paint', 'Seat', None]
}

students_df = pd.DataFrame(students_data)
print(f"Practice 1: \n", students_df)

print("********************************************\n")
print(f"Знаходимо всіх студентів, вік яких понад 20 років.\n")

older_students = students_df[students_df['Вік'] >= 20]
print(older_students)
print("********************************************\n")


print(f"Зберігаємо оброблені дані в новий CSV-файл.")

students_df.to_csv('./students.csv', index=False)

print("********************************************\n")
print(f"Зчитуємо дані з CSV-файлу та виводимо перші 5 рядків. Метод head\n")

file_path = './students.csv'
data_df = pd.read_csv(file_path)
print(data_df.head())

print("********************************************\n")
print(f"Виведення розміру DataFrame")

print("Print of DataFrame. \n", data_df.shape)

print("********************************************\n")
print(f"Отримаємо опис статистичних характеристик за допомогою методу describe.\n")

print(data_df.describe())


data_df.describe(percentiles=None, include='all', exclude=None)
print("********************************************\n")


print(f"загальну інформацію про DataFrame методом info")

data_df.info()
print("********************************************\n")
print(f"Та нарешті побудуємо гістограму для вікової групи студентів.")

students_df['Вік'].plot(kind='bar', title='Вікова група студентів')
plt.show()

import sys


data_df.info(verbose=True, buf=sys.stdout, max_cols=None, memory_usage='deep', show_counts=True)