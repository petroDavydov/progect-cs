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

students_data2 = students_df.loc[students_df['Вік'] >= 22]
print(students_data2)

students_math = students_df.loc[students_df['Спеціальність'] == 'Math']
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
print("********************************************\n")

print(f"Сортування даних")

students_sort = students_df.sort_values(by='Вік', ascending=True)
print(f"This is sort by year: \n", students_sort)
print("********************************************\n")

print(f"Очищення даних за допомогою Pandas \n")

students_data = {
    'Імена': ['Anna', 'Bohdan', None],
    'Вік': [21, None, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

cleaned_df = students_df.dropna()
print(cleaned_df)
print("********************************************\n")

print(f"Метода fillna заповнює відсутні дані вказаним значенням або методом.\n")

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

data = data.fillna({0: data[0].mean(), 1: data[1].mean(), 2: data[2].mean()})

print(data)
print("********************************************\n")

print(f"Метод drop використовується для видалення конкретних рядків або стовпців з DataFrame.\n")

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

# students_df.drop([1], inplace=True)
# print(f"Використовуючи [1] та inplace=True: \n", students_df)

students_df.drop(['Вік'], axis=1)
print(f"Використовуючи axis=1: \n", students_df)
print("********************************************\n")

print(f"Конвертація типів та стандартизація даних")

print(f"Необхідно виконати конвертація віку в цілочисельний тип, використовуючи astype: \n")

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21.0, 22.0, 20.0],  # Вік як float
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

# Конвертація типу стовпця 'Вік' в int

students_df['Вік'] = students_df['Вік'].astype(int)
print(f"Use astype and .dtypes: \n", students_df.dtypes)
print("********************************************\n")


students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'PHYSICS', 'biology']
}

students_df = pd.DataFrame(students_data)

# Приведення спеціальностей до нижнього регістру
students_df['Спеціальність'] = students_df['Спеціальність'].str.lower()
print(f"Use .str.lower: \n", students_df)
print("********************************************\n")


# Середні температури за дні місяця
temperature_data = {
    'День': list(range(1, 31)),
    'Температура': [15, 18, None, 20, 17, 18, 20, None, 14, 16, 18, 19,
                    None, 15, 14, 17, 16, None, 17, 20, 15, 16, 15, 19,
                    20, None, 15, 18, 17, 16]
}

temperature_df = pd.DataFrame(temperature_data)

# Знаходження середньої температури за місяць, виключаючи відсутні значення
mean_temperature = temperature_df['Температура'].mean()

# Заміна відсутніх значень температури середньою температурою за місяць
temperature_df['Температура'].fillna(mean_temperature, inplace=True)
# Second variant: temperature_df.fillna({'Температура' : mean_temperature}, inplace=True)
# Third variant : temperature_df['Температура'] = temperature_df['Температура'].fillna(mean_temperature)
print(f"Use filna and mean(): \n", temperature_df)
print("********************************************\n")

print(f"Дублікати можуть спотворювати результати аналізу. Для видалення дублюючих даних можна використовувати метод drop_duplicates: \n")

data = {
    "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
    "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
    "age": [25, 32, 19, 23, 19, 23]
}

employees = pd.DataFrame(data)

employees = employees.drop_duplicates()
print(f"Use drop_duplicates(): \n", employees)
print("********************************************\n")

pd.set_option('future.no_silent_downcasting', True)  # for futur behavior
data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура': [25, 28, 24],
    'Вологість': ['висока', 'низька', 'висока']
}

weather_df = pd.DataFrame(data)
weather_df['Вологість'].replace({'висока': 80, 'низька': 30}, inplace=True)
# weather_df.infer_objects(copy=False) #for future behavior


print(f"Use replace: \n", weather_df)
print("********************************************\n")
