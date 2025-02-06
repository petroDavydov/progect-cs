import seaborn as sns
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# students_data = {
#     'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Maria', 'Petro', 'Sophia', 'Max', 'Natalia', 'Vadym'],
#     'Вік': [21, 22, 20, 19, 23, 22, 21, 20, 19, 21],
#     'Спеціальність': ['Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics'],
#     'Хобі': ['Jump', 'Read', 'Swim', 'Look', 'Eat', 'Work', 'Write', 'Paint', 'Seat', None]
# }

# students_df = pd.DataFrame(students_data)
# print(f"Practice 1: \n", students_df)

# print("********************************************\n")
# print(f"Знаходимо всіх студентів, вік яких понад 20 років.\n")

# older_students = students_df[students_df['Вік'] >= 20]
# print(older_students)
# print("********************************************\n")


# print(f"Зберігаємо оброблені дані в новий CSV-файл.")

# students_df.to_csv('./students.csv', index=False)

# print("********************************************\n")
# print(f"Зчитуємо дані з CSV-файлу та виводимо перші 5 рядків. Метод head\n")

# file_path = './students.csv'
# data_df = pd.read_csv(file_path)
# print(data_df.head())

# print("********************************************\n")
# print(f"Виведення розміру DataFrame")

# print("Print of DataFrame. \n", data_df.shape)

# print("********************************************\n")
# print(f"Отримаємо опис статистичних характеристик за допомогою методу describe.\n")

# print(data_df.describe())


# data_df.describe(percentiles=None, include='all', exclude=None)
# print("********************************************\n")


# print(f"загальну інформацію про DataFrame методом info")

# data_df.info()
# print("********************************************\n")
# print(f"Та нарешті побудуємо гістограму для вікової групи студентів.")

# # students_df['Вік'].plot(kind='bar', title='Вікова група студентів')
# # plt.show()


# data_df.info(verbose=True, buf=sys.stdout, max_cols=None,
#              memory_usage='deep', show_counts=True)
# print("********************************************\n")

# print(f"Робота з даними в Pandas та агрегація даних")

# students_df = pd.DataFrame({
#     'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna', 'Mykola'],
#     'Вік': [21, 22, 20, 21, 23, 20],
#     'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics', 'Geography'],
#     'Хобі': ['Sweem', 'Jump', 'Fly', 'Ride', 'Run', 'Nothing']
# }, index=['st1', 'st2', 'st3', 'st4', 'st5', 'st6'])

# print(f"This is begin frame: \n", students_df)
# print("********************************************\n")

# print(f"Зробимо вибірку за віком з 'st2', за допомогою .loc : \n")

# value = students_df.loc['st2', 'Вік']
# print(value)  # 22

# print(f"Вибірка зрізу рядків та стовпців за мітками можна виконати наступним чином: \n")

# subset = students_df.loc['st2':'st4', 'Імена':'Вік']
# print(subset)

# print(f"Якщо ми хочемо вибірку за декількома конкретними мітками: \n")

# subset1 = students_df.loc[['st3', 'st6'], ['Вік', 'Хобі', 'Імена']]
# print(f"This is subset1: \n", subset1)


# print(f"Метод iloc використовується для вибірки даних за числовими індексами, та має наступний синтаксис:\n")
# print(f"Виконаємо такі самі вибірки, але тепер за допомогою методу iloc. Вибірка конкретного рядка та стовпця за індексами\n")

# value = students_df.iloc[1, 2]
# print(value)
# print("********************************************\n")

# subset = students_df.iloc[1:4, 0:2]
# print(subset)

# subset = students_df.iloc[[0, 2], [0, 2]]
# print(subset)
# print("********************************************\n")

# students_data = students_df.loc[(students_df['Спеціальність'] == 'Physics') & (
#     students_df['Хобі'] == 'Run') & (students_df['Вік'] == 23)]
# print(students_data)

# students_data2 = students_df.loc[students_df['Вік'] >= 22]
# print(students_data2)

# students_math = students_df.loc[students_df['Спеціальність'] == 'Math']
# print(students_math)
# print("********************************************\n")

# # -----------------------------------------------------


# students_data = {
#     'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
#     'Вік': [21, 22, 20, 21, 23],
#     'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
# }

# students_df = pd.DataFrame(students_data)
# print(students_df)
# print("********************************************\n")

# grouped_by = students_df.groupby('Спеціальність')
# mean_age = grouped_by['Вік'].mean()
# print(f"Middle age of students: \n", mean_age)

# print(f"Знайдемо мінімальний та максимальний вік студентів за спеціальностями, за допомогою .agg :\n")

# min_max_age = grouped_by['Вік'].agg(['min', 'max'])
# print(f"This is min-max: \n", min_max_age)
# print("********************************************\n")

# summury = grouped_by.agg({
#     'Вік': ['min', 'max', 'mean'],
#     'Імена': 'count'
# })

# print(f"This is grouped_by.agg: \n", summury)

# print(f"лямбда-функція для обчислення різниці між максимальним та мінімальним віком студентів в кожній спеціальності: \n")

# result = grouped_by['Вік'].agg(lambda x: x.max() - x.min())
# print(f"Use lambda function: \n", result)
# print("********************************************\n")

# print(f"Використання функцій агрегації")

# age_result = students_df['Вік'].sum()
# print(f"This is age of  all students: \n", age_result)

# age_result_mean = students_df['Вік'].mean()
# print(f"This is mean age of  all students: \n", age_result_mean)

# age_result_median = students_df['Вік'].median()
# print(f"This is median age of  all students: \n", age_result_median)


# age_result_min = students_df['Вік'].min()
# print(f"This is min age of  all students: \n", age_result_min)

# age_result_max = students_df['Вік'].max()
# print(f"This is max age of students: \n", age_result_max)

# age_result_std = students_df['Вік'].std()
# print(f"This is std age of students: \n", age_result_std)

# age_result_var = students_df['Вік'].var()
# print(f"This is dispersion: \n", age_result_var)

# age_result_not_empty = students_df['Вік'].count()
# print(f"This is not empty result: \n", age_result_not_empty)

# unique_result = students_df['Спеціальність'].nunique()
# print(f"This is unique result: \n", unique_result)

# quantile_result = students_df['Вік'].quantile(0.25)
# print(f"This is quantile result: \n", quantile_result)


# idx_max_age = students_df['Вік'].idxmax()
# print(f"idxmax() знаходить індекс максимального значення: \n", idx_max_age)

# idx_min_age = students_df['Вік'].idxmin()
# print(f"Індекс мінімального значення idxmin(): \n", idx_min_age)

# product_age = students_df['Вік'].prod()
# print(f"Метод prod() знаходить добуток всіх значень: \n ", product_age)

# sem_age = students_df['Вік'].sem()
# print(f"Стандартна помилка середнього метод sem(): \n", sem_age)
# print("********************************************\n")

# print(f"Сортування даних")

# students_sort = students_df.sort_values(by='Вік', ascending=True)
# print(f"This is sort by year: \n", students_sort)
# print("********************************************\n")

# print(f"Очищення даних за допомогою Pandas \n")

# students_data = {
#     'Імена': ['Anna', 'Bohdan', None],
#     'Вік': [21, None, 20],
#     'Спеціальність': ['Math', 'Physics', 'Biology']
# }

# students_df = pd.DataFrame(students_data)

# cleaned_df = students_df.dropna()
# print(cleaned_df)
# print("********************************************\n")

# print(f"Метода fillna заповнює відсутні дані вказаним значенням або методом.\n")

# data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

# data = data.fillna({0: data[0].mean(), 1: data[1].mean(), 2: data[2].mean()})

# print(data)
# print("********************************************\n")

# print(f"Метод drop використовується для видалення конкретних рядків або стовпців з DataFrame.\n")

# students_data = {
#     'Імена': ['Anna', 'Bohdan', 'Olena'],
#     'Вік': [21, 22, 20],
#     'Спеціальність': ['Math', 'Physics', 'Biology']
# }

# students_df = pd.DataFrame(students_data)

# # students_df.drop([1], inplace=True)
# # print(f"Використовуючи [1] та inplace=True: \n", students_df)

# students_df.drop(['Вік'], axis=1)
# print(f"Використовуючи axis=1: \n", students_df)
# print("********************************************\n")

# print(f"Конвертація типів та стандартизація даних")

# print(f"Необхідно виконати конвертація віку в цілочисельний тип, використовуючи astype: \n")

# students_data = {
#     'Імена': ['Anna', 'Bohdan', 'Olena'],
#     'Вік': [21.0, 22.0, 20.0],  # Вік як float
#     'Спеціальність': ['Math', 'Physics', 'Biology']
# }

# students_df = pd.DataFrame(students_data)

# # Конвертація типу стовпця 'Вік' в int

# students_df['Вік'] = students_df['Вік'].astype(int)
# print(f"Use astype and .dtypes: \n", students_df.dtypes)
# print("********************************************\n")


# students_data = {
#     'Імена': ['Anna', 'Bohdan', 'Olena'],
#     'Вік': [21, 22, 20],
#     'Спеціальність': ['Math', 'PHYSICS', 'biology']
# }

# students_df = pd.DataFrame(students_data)

# # Приведення спеціальностей до нижнього регістру
# students_df['Спеціальність'] = students_df['Спеціальність'].str.lower()
# print(f"Use .str.lower: \n", students_df)
# print("********************************************\n")


# # Середні температури за дні місяця
# temperature_data = {
#     'День': list(range(1, 31)),
#     'Температура': [15, 18, None, 20, 17, 18, 20, None, 14, 16, 18, 19,
#                     None, 15, 14, 17, 16, None, 17, 20, 15, 16, 15, 19,
#                     20, None, 15, 18, 17, 16]
# }

# temperature_df = pd.DataFrame(temperature_data)

# # Знаходження середньої температури за місяць, виключаючи відсутні значення
# mean_temperature = temperature_df['Температура'].mean()

# # Заміна відсутніх значень температури середньою температурою за місяць
# # temperature_df['Температура'].fillna(mean_temperature, inplace=True)
# temperature_df.fillna({'Температура' : mean_temperature}, inplace=True) #Second Variant, work witout "warning"
# # Third variant : temperature_df['Температура'] = temperature_df['Температура'].fillna(mean_temperature)
# print(f"Use filna and mean(): \n", temperature_df)
# print("********************************************\n")

# print(f"Дублікати можуть спотворювати результати аналізу. Для видалення дублюючих даних можна використовувати метод drop_duplicates: \n")

# data = {
#     "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
#     "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
#     "age": [25, 32, 19, 23, 19, 23]
# }

# employees = pd.DataFrame(data)

# employees = employees.drop_duplicates()
# print(f"Use drop_duplicates(): \n", employees)
# print("********************************************\n")

# pd.set_option('future.no_silent_downcasting', True)  # for future behavior
# data = {
#     'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
#     'Температура': [25, 28, 24],
#     'Вологість': ['висока', 'низька', 'висока']
# }

# weather_df = pd.DataFrame(data)
# # weather_df['Вологість'].replace({'висока': 80, 'низька': 30}, inplace=True)
# weather_df.infer_objects(copy=False) #for future behavior
# weather_df.replace({'Вологість': 80}, {'Вологість': 30}, inplace=True) #new variant, wark without "warning"


# print(f"Use replace: \n", weather_df)
# print("********************************************\n")

# print(f"Робота з датами")

# date = pd.Timestamp("2021-09-10")

# print(f"Use Tamestamp,(Одинична чісова мітка):\n", date)
# print("********************************************\n")

# date = pd.to_datetime("2021-09-10 2:54:13")

# print(f"Use to_datetime(для конвертації рядкових дат в datetime об'єкти): \n", date)
# print("********************************************\n")

# print("""Наприклад, створимо DatetimeIndex — ряд часових міток з відсіченням в один день
#        тривалістю вісім днів, змінна date. На основі отриманого об'єкта створимо структуру
#        Series з денною температурою у місті Полтава у ці дні.""")

# date = pd.date_range(start='2021-09-01', freq='D', periods=8)
# print(f"date info DatetimeIndex: \n", date)

# temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)

# print("Use data_range: \n", temperature)

# print("********************************************\n")

# print("""Підіб'ємо підсумок та створимо прикладний набір даних з деякими поширеними проблемами,
# такими як відсутні дані, дублікати та неправильні типи даних, та покажемо, як виправити
# ці проблеми за допомогою відповідних функцій Pandas, що ми розглянули.""")

# data = {
#     'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', None, 'Львів'],
#     'Температура': [25, 32, None, 24, 23, 32],
#     'Вологість': ['60%', '70%', '65%', '55%', None, '70%'],
#     'Дата': ['2021-08-01', '2021-08-01', '2021-08-02', '2021-08-02', '2021-08-03', '2021-08-01']
# }
# df = pd.DataFrame(data)

# print(f"Start DataFrame:\n", df)
# print("********************************************\n")

# df.drop_duplicates(subset=['Місто', 'Дата'], inplace=True) # drop duplicate
# df.dropna(subset=['Місто'], inplace=True) # видалити рядки з відсутніми значеннями
# # df['Температура'].fillna(df['Температура'].mean(), inplace=True) # заповнити відсутні дані середнім значенням температури
# df.fillna({'Температура': df['Температура'].mean()}, inplace=True) # work without warning
# # ---
# # Останнім ми конвертуємо "Вологість" в число, видаливши знак відсотка та конвертуємо "Дата" в об'єкт datetime.
# # df['Вологість'] = df['Вологість'].str.rstrip('%').astype('float') / 100
# df.replace({'Вологість': {r'%$': ''}}, regex=True, inplace=True) # work wiyhout warning
# df['Вологість'] = df['Вологість'].astype('float') / 100 # work without warning
# df['Дата'] = pd.to_datetime(df['Дата']) # конвертуємо "Дата" в об'єкт datetime

# print(f"Print after cleaning: \n", df)
# print("********************************************\n")

# print(f"Об'єднання DataFrame")

# data1 = {
#     "name": {"1": "Michael", "2": "John"},
#     "country": {"1": "Canada", "2": "USA"},
#     "age": {"1": 25, "2": 32}
# }

# print("Beginning-Zero Data: \n", data1)

# employees1 = pd.DataFrame(data1)
# print(f"First dataframe employees1: \n", employees1)

# data2 = {
#     "name": {"3": "Liza", "4": "Jhon"},
#     "country": {"3": "Australia", "4": "Denmark"},
#     "age": {"3": 19, "4": 23}
# }

# employees2 = pd.DataFrame(data2)
# print(f"Second dataframe employees2: \n", employees2)


# employees = pd.concat([employees1, employees2])

# print(f"Use CONCAT with dataframe employees1 and dataframe employees2: \n", employees)
# print("********************************************\n")

# data1 = {
#     "name": ["Michael", "John"],
#     "country": ["Canada", "USA"],
# }

# data2 = {
#     "name": ["Michael", "Liza"],
#     "age": [25, 19]
# }

# employees1 = pd.DataFrame(data1)
# employees2 = pd.DataFrame(data2)

# employees2 = employees2.set_index("name")

# merged = pd.merge(employees1, employees2, on='name', how='outer')

# print(f"Use MERGE with data frame employees1 and employees2: \n", merged)
# print("********************************************\n")

# employees1 = pd.DataFrame(data1).set_index("name")
# employees2 = pd.DataFrame(data2).set_index("name")

# joined = employees1.join(employees2, how="outer")

# print(f"Use JOIN with data frame employees1 and employees2: \n", joined)
print("********************************************\n")

print(f"Застосування функцій до даних\n")

data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура C': [25, 28, 24]
}

weather_df = pd.DataFrame(data)

print(f"Start data weather_df: \n", weather_df)


weather_df['Температура F'] = weather_df['Температура C'].apply(
    lambda temp: (temp * 9/5) + 32)

print(weather_df)

print("********************************************\n")
# Дані про продукти та їх ціни та знижки
data = {
    'Product': ['iPhone 13', 'MacBook Pro', 'Apple Watch'],
    'Price': [699, 1299, 399],
    'Discount': [0.1, 0.05, 0.15]
}

# Створення DataFrame з цими даними
df = pd.DataFrame(data)

# Застосування lanbda-функції до кожного рядка за допомогою apply з axis=1
df['Final Price'] = df.apply(
    lambda row: row['Price'] * (1 - row['Discount']), axis=1)

print(f"Use to each raw axis=1, apply, lambda: \n", df)
print("********************************************\n")

# Дані про товари та їх ціни
data = {
    'iPhone 13 (64GB)': [699, 799],
    'MacBook Pro (13-inch)': [1299, 1499]
}

# Створення DataFrame з цінами
df = pd.DataFrame(data)

# Застосування 10% знижки до всіх цін за допомогою applymap і лямбда-функції
# df_discounted = df.applymap(lambda price: price * 0.9) ## applymap is depricated
df_discounted = df.map(lambda price: price * 0.9)
print(f"Use map (applymap-> depricated) for all costs: \n", df_discounted)
print("********************************************\n")

print(f"Створення pivot_table\n")

df = pd.DataFrame({
    "Фрукт": ["Яблуко", "Яблуко", "Груша", "Груша", "Банан", "Банан"],
    "Колір": ["Червоний", "Зелений", "Жовтий", "Зелений", "Жовтий", "Зелений"],
    "Кількість": [10, 12, 15, 9, 20, 18],
    "Ціна": [5, 4, 6, 7, 3, 2]
})

print("Start data conneting with pivot_table topic: \n", df)
print("********************************************\n")

table = df.pivot_table(values="Ціна", index="Фрукт", columns="Колір")

print("Таблиця table з середньою ціною по фруктах і кольорах: \n", table)
print("********************************************\n")

table = df.pivot_table(values="Ціна", index="Фрукт",
                       columns="Колір", margins=True, fill_value=0)

print("""Додамо загальну суму по рядках і стовпцях 
      і заповнимо пропущені значення нулями: \n""", table)
print("********************************************\n")

# Завантаження набору даних "Titanic"
titanic = sns.load_dataset('titanic')

# Виведення перших 5 рядків
print(f"Use seaborn, pivot_table. Start data: \n", titanic.head())
print("********************************************\n")


# Створення зведеної таблиці
pivot_table = pd.pivot_table(titanic, values='age', index=['class'], columns=[
                             # add observed=False - for future behavior
                             'sex'], aggfunc='mean', observed=False)

# Виведення зведеної таблиці
print('''згрупувати дані за класом кают (стовпець "class")
та статтю (стовпець "sex") і розрахувати середній вік для кожної групи. \n''', pivot_table)
print("********************************************\n")

# Створення зведеної таблиці з двома рівнями індексу
pivot_table = pd.pivot_table(titanic, values='age', index=[
                             'class', 'survived'], columns=['sex'], aggfunc='mean', observed=True)

# Виведення зведеної таблиці
print("додати ще один рівень ієрархії до індексу, наприклад, за стовпцем survived:  \n", pivot_table)
print("********************************************\n")

# Створення зведеної таблиці з різними функціями агрегації
pivot_table = pd.pivot_table(titanic, values=['fare', 'survived'], index=[
                             'class', 'sex'], aggfunc={'fare': 'mean', 'survived': 'count'}, observed=False)

# Виведення зведеної таблиці
print(f"застосувати різні функції агрегації до різних стовпців: \n", pivot_table)
print("********************************************\n")

