from numpy import median
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = sns.load_dataset("mpg")  # Данні з якими працюємо
print(f"DataSet named mpg, first 10 line: \n", data.head(10))
# ----------------------------


sns.set_style('darkgrid')
sns.lineplot(x='model_year', y='horsepower', hue='origin', hue_order=['japan', 'europe', 'usa'],
             data=data)  # залежність потужності від року випуску

plt.title("Залежність потужності від року випуску")
plt.show()
# ----------------------------
print("******************************************\n")

print(f"Функція scatterplot\n")

sns.scatterplot(x='mpg', y='displacement', hue='origin', data=data)

plt.title("Функція scatterplot")
plt.show()
# --------------------------------------------------
print("******************************************\n")

print(f"Функція relplot \n")

sns.relplot(x='mpg', y='displacement', kind='scatter',
            hue='origin', col='origin', data=data)

plt.title("Функція relplot")
plt.show()
# --------------------------------------------------
print("******************************************\n")

print(f"Візуалізація категоріальних даних\n")

print(f"Функція stripplot: \n")

sns.stripplot(x='origin', y='mpg', hue='cylinders', data=data)

plt.title("Функція stripplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print(f"Функція swarmplot: \n")

palette = {'usa': 'blue', 'japan': 'orange',
           'europe': 'green'}  # додано самостійно для розуміння контролю кольорів
sns.swarmplot(x='origin', y='mpg', hue='origin',
              palette=palette, data=data)  # додано hue, palette

plt.title("Функція swarmplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print(f"Візуалізації розподілу категоріальних даних\n")
print("""boxplot — будує діаграму типу "скринька з вусами",
    на ній відображаються медіанне значення, квартілі та викиди\n""")


palette = {3: 'red', 4: 'yellow', 5: 'green', 6: 'blue', 8: 'orange'}
sns.boxplot(x='origin', y='mpg', hue='cylinders', palette=palette, data=data)
print(data.dtypes)

plt.title("Функція boxplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print(f"violinplot — будує діаграму, схожу на 'скриньку з вусами' з оцінкою щільності ядра\n")


# додано для контродю за кольорами
palette = {'usa': 'blue', 'japan': 'green', 'europe': 'red'}
sns.violinplot(x='origin', y='mpg', palette=palette, hue='origin',
               legend=False, data=data)  # додано palette, hue, legend

plt.title("Функція violinplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print("""boxenplot — будує діаграму з прямокутників,
    добре підходить для візуалізації великих наборів даних.\n""")

# додано для контролю за кольорами
palette = {'usa': 'blue', 'japan': 'green', 'europe': 'red'}
sns.boxenplot(x='origin', y='mpg', hue='origin',
              palette=palette, legend=False, data=data)  # додано hue, legend, palette

plt.title("Функція boxenplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print(f"Візуалізація оцінок категоріальних даних\n")

print(f"Функція pointplot \n")
print("""Відображає оцінку будь-якого набору даних
        як точку на полі графіка та довірчий інтервал у вигляді лінії,
        центр якої лежить на зазначеній точці.""")

sns.pointplot(x='origin', y='mpg', data=data)

plt.title("Функція pointplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print("""Функція barplot\n
Функція будує стовпчасту діаграму:
висота бару (стовпця) визначає чисельне значення оцінки ознаки (математичне очікування),
лінія, що перетинає верхню межу бару - довірчий інтервал.""")


palette = {'usa': 'blue', 'japan': 'green', 'europe': 'red'}
sns.barplot(x='origin', y='mpg', hue='origin',
            legend=False, palette=palette, data=data)

plt.title("Функція barplot")
plt.show()
# ------------------------------------------------------
print("******************************************\n")

print("""Функція countplot\nФункція визначає кількість елементів з набору даних,
які належать до тієї або іншої категорії, і відображає отримане значення
у вигляді стовпчастої діаграми.""")

palette = {3: 'red', 4: 'yellow', 5: 'green',
           6: 'blue', 8: 'orange'}  # для контролю за кольорами
sns.countplot(x='cylinders', palette=palette, hue='cylinders',
              legend=False, data=data)  # додано hue, legend, palette

plt.title("Функція countplot")
plt.show()
print("******************************************\n")
print(f"Візуалізація моделі лінійної регресії\n")


# sns.regplot(x="horsepower", y="displacement", data=data) # ???
# sns.regplot(x="horsepower", y="displacement", data=data)
sns.regplot(x="horsepower", y="displacement", data=data, x_estimator=median)
# sns.regplot(x="horsepower", y="displacement", data=data, x_bins=100)
# sns.regplot(x="horsepower", y="displacement", data=data, x_ci=[20,30])

plt.title("Функція regplot")
plt.show()
print("******************************************\n")

print(f"Функція residplot\n")

sns.residplot(x="horsepower", y="displacement", data=data)

plt.title("Функція residplot")
plt.show()

print("******************************************\n")

print(f"Функція lmplot\n")
# sns.set_palette(sns.color_palette('Blues')) # add colors what need
sns.lmplot(x="horsepower", y="displacement",
           data=data, hue="origin", col="origin")

plt.title("Функція lmplot")
plt.show()
print("******************************************\n")
