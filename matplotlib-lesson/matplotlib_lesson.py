import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(figsize=(10, 4))
axs.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs.plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')
axs.plot(date, [20, 15, 23, 5, 7, 20, 41, -2], label='morning temperature')
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.text(date[0], 21, 'Друга лінія', color="blue")
plt.text(date[0], 10, 'Третя лінія', color="green")

plt.legend()
plt.show()

print("********************************************\n")
print("Якщо поділити графіки, то: fig, axs = plt.subplots(2, 1, figsize=(10, 6)): \n")
date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')

axs[0].set_title('Денна', fontsize=10)
axs[1].set_title('Нічна', fontsize=10)

fig.suptitle('Температура в м. Полтава', fontsize=15)

plt.show()

print("********************************************\n")
print("""Якщо управляти стилем графіків, то:
plt.plot(date, [<num>, <num>...], label="...",
linestyle=": ", color=' ',""")

date = pd.date_range(start="2021-09-01", freq="D", periods=8)
plt.figure(figsize=(10, 4))  # Збільшення ширини графіка до 10 дюймів
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label="day temperature",
    linestyle="--",
    color="#FF5733",
)
plt.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11, 16],
    label="night temperature",
    linestyle="-.",
    color="#061358",
)
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.show()
print("********************************************\n")

date = pd.date_range(start="2021-09-01", freq="H", periods=8)
print("This is data pd.data_range: \n", date)
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label="day temperature",
    linestyle="-.",
    color="#FF5733",
    linewidth=2,
    marker="D",
)
plt.plot(
    date,  # датасет з яким працюємо
    [19, 11, 16, 11, 10, 10, 11, 16],
    label="night temperature",
    linestyle=":",  # стиль лінії
    color="#061358",
    linewidth=3,  # товщина лінії
    marker="*",  # встановлення маркера
)
plt.ylim(0, 25)  # Остаточне значення
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.grid()  # відображення сітки
plt.show()
print("********************************************\n")

plt.bar(
    ["США", "Китай", "Японія", "Велика Британія"],
    [39, 38, 27, 22],
    color=["b", "r", "y", "g"],
)

plt.xlabel("Країна", fontsize="small", color="midnightblue")
plt.ylabel("Кількість", fontsize="small", color="midnightblue")
plt.title("Золоті медалі: Літня олімпіада Токіо 2020", fontsize=15)
plt.show()
print("********************************************\n")


countries = ["США", "Китай", "Японія", "Велика Британія", "Україна"]
counts = [39, 38, 27, 22, 88]
colors = ["b", "r", "y", "g", "c"]

bars = plt.bar(
    countries,
    counts,
    color=colors,
    width=0.6
)

# Додати штрихування до певного стовбчика
bars[0].set_hatch("|")
bars[1].set_hatch("/")
bars[2].set_hatch("-")  # Додаємо штрихування до третього стовбчика (Японія)
bars[3].set_hatch("o")
bars[4].set_hatch("X")


plt.xlabel("Країна", fontsize="small", color="midnightblue")
plt.ylabel("Кількість", fontsize="small", color="midnightblue")
plt.title("Золоті медалі: Літня олімпіада Токіо 2020", fontsize=15)
plt.show()
print("********************************************\n")


labels = [
    "Junior Software Engineer",
    "Senior Software Engineer",
    "Software Engineer",
    "System Architect",
    "Technical Lead",
]

data = [63, 31, 100, 2, 11]
explode = [0.15, 0.18, 0.18, 0.13, 0.1]
plt.pie(
    data,
    labels=labels,
    shadow=False,
    explode=explode,
    autopct="%.2f%%",
    pctdistance=1.15,
    labeldistance=1.3,
)

plt.show()
print("********************************************\n")

print(f"Діаграми в полярних координатах\n")

# Для отримання графіка в полярних координатах (r,θ) використовується метод polar,
# в який передаються аргументи theta (незалежна змінна) і r.

print('графік полярної троянди: r(θ)=sin⁡(6⋅θ)\n')

theta = np.linspace(0, 2.0 * np.pi, 1000)

r = np.sin(9 * theta)
plt.polar(theta, r, color="c", linestyle='--',
          linewidth=2,
          #         marker='x',
          #         markersize=3,
          #         alpha=0.75
          )
plt.show()

print("********************************************\n")

print(f"Тривимірні графіки \n")

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

theta_max = 8 * np.pi
n = 1000
theta = np.linspace(0, theta_max, n)
x = theta
z = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z, "r")

plt.show()
print("********************************************\n")

fig = plt.figure()  # створнення фігури
ax = fig.add_subplot(projection="3d")  # додавання тривимірної проєкції

x = [5, 10, 15, 20, 4, 55, 33]
z = [10, 0, 5, 15, 76, 22, 11]
y = [0, 10, 5, 25, 34, 99, 44]
s = [150, 130, 30, 160, 200, 22, 78]
ax.scatter(x, y, z, s=s)  # створення діаграми розсіювання

plt.show()
print("********************************************\n")

print(f"Каркасна поверхня\n")

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)  # сворення масиву значень
x, y = np.meshgrid(grid, grid)  # створення двовимірної сітки координат
# Обчислює значення z для кожної пари координат x і y за допомогою функції 𝑧=𝑥2⋅𝑦2+2.
z = x ** 2 * y ** 2 + 2

# Створює тривимірний каркасний графік на основі значень x,y,z
# ax.plot_wireframe(x, y, z)
ax.plot_surface(x, y, z)  # побудова поврхні

plt.show()
print("********************************************\n")
