import sys
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

# students_df['Вік'].plot(kind='bar', title='Вікова група студентів')
# plt.show()


data_df.info(verbose=True, buf=sys.stdout, max_cols=None,
             memory_usage='deep', show_counts=True)
print("********************************************\n")

print(f"Робота з даними в Pandas та агрегація даних")

students_df = pd.DataFrame({
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna', 'Mykola'],
    'Вік': [21, 22, 20, 21, 23, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics', 'Geography'],
    'Хобі': ['Sweem', 'Jump', 'Fly', 'Ride', 'Run', 'Nothing']
}, index=['st1', 'st2', 'st3', 'st4', 'st5', 'st6'])

print(f"This is begin frame: \n", students_df)
print("********************************************\n")

print(f"Зробимо вибірку за віком з 'st2', за допомогою .loc : \n")

value = students_df.loc['st2', 'Вік']
print(value)  # 22

print(f"Вибірка зрізу рядків та стовпців за мітками можна виконати наступним чином: \n")

subset = students_df.loc['st2':'st4', 'Імена':'Вік']
print(subset)

print(f"Якщо ми хочемо вибірку за декількома конкретними мітками: \n")

subset1 = students_df.loc[['st3', 'st6'], ['Вік', 'Хобі', 'Імена']]
print(f"This is subset1: \n", subset1)


print(f"Метод iloc використовується для вибірки даних за числовими індексами, та має наступний синтаксис:\n")
print(f"Виконаємо такі самі вибірки, але тепер за допомогою методу iloc. Вибірка конкретного рядка та стовпця за індексами\n")

value = students_df.iloc[1, 2]
print(value)
print("********************************************\n")

subset = students_df.iloc[1:4, 0:2]
print(subset)

subset = students_df.iloc[[0, 2], [0, 2]]
print(subset)
print("********************************************\n")

students_data = students_df.loc[(students_df['Спеціальність'] == 'Physics') & (
    students_df['Хобі'] == 'Run') & (students_df['Вік'] == 23)]
print(students_data)

students_data2 = students_df.loc[students_df['Вік']>=22]
print(students_data2)

students_math = students_df.loc[students_df['Спеціальність']=='Math']
print(students_math)
print("********************************************\n")

# -----------------------------------------------------


students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)
print(students_df)
print("********************************************\n")

grouped_by = students_df.groupby('Спеціальність')
mean_age = grouped_by['Вік'].mean()
print(f"Middle age of students: \n", mean_age)

print(f"Знайдемо мінімальний та максимальний вік студентів за спеціальностями, за допомогою .agg :\n")

min_max_age = grouped_by['Вік'].agg(['min', 'max'])
print(f"This is min-max: \n", min_max_age)
print("********************************************\n")

summury = grouped_by.agg({
    'Вік': ['min', 'max', 'mean'],
    'Імена': 'count'
})

print(f"This is grouped_by.agg: \n", summury)

print(f"лямбда-функція для обчислення різниці між максимальним та мінімальним віком студентів в кожній спеціальності: \n")

result = grouped_by['Вік'].agg(lambda x: x.max() - x.min())
print(f"Use lambda function: \n", result)
print("********************************************\n")

print(f"Використання функцій агрегації")

age_result = students_df['Вік'].sum()
print(f"This is age of  all students: \n", age_result)

age_result_mean = students_df['Вік'].mean()
print(f"This is mean age of  all students: \n", age_result_mean)

age_result_median = students_df['Вік'].median()
print(f"This is median age of  all students: \n", age_result_median)


age_result_min = students_df['Вік'].min()
print(f"This is min age of  all students: \n", age_result_min)

age_result_max = students_df['Вік'].max()
print(f"This is max age of students: \n", age_result_max)

age_result_std = students_df['Вік'].std()
print(f"This is std age of students: \n", age_result_std)

age_result_var = students_df['Вік'].var()
print(f"This is dispersion: \n", age_result_var)

age_result_not_empty = students_df['Вік'].count()
print(f"This is not empty result: \n", age_result_not_empty)

unique_result = students_df['Спеціальність'].nunique()
print(f"This is unique result: \n", unique_result)

quantile_result = students_df['Вік'].quantile(0.25)
print(f"This is quantile result: \n", quantile_result)


idx_max_age = students_df['Вік'].idxmax()
print(f"idxmax() знаходить індекс максимального значення: \n", idx_max_age)

idx_min_age = students_df['Вік'].idxmin()
print(f"Індекс мінімального значення idxmin(): \n", idx_min_age)

product_age = students_df['Вік'].prod()
print(f"Метод prod() знаходить добуток всіх значень: \n ", product_age)

sem_age = students_df['Вік'].sem()
print(f"Стандартна помилка середнього метод sem(): \n", sem_age)
