import pandas as pd
import matplotlib.pyplot as plt


# date = pd.date_range(start='2021-09-01', freq='D', periods=8)
# fig, axs = plt.subplots(figsize=(10, 4))
# axs.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
# axs.plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')
# plt.xlabel('Дата', fontsize='small', color='midnightblue')
# plt.ylabel('Температура', fontsize='small', color='midnightblue')
# plt.title('Температура в м. Полтава', fontsize=15)
# plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
# plt.text(date[0], 21, 'Друга лінія', color="blue")

# plt.legend()
# plt.show()

# print("********************************************\n")
# print("Якщо поділити графіки, то: fig, axs = plt.subplots(2, 1, figsize=(10, 6)): \n")
# date = pd.date_range(start='2021-09-01', freq='D', periods=8)
# fig, axs = plt.subplots(2, 1, figsize=(10, 6))

# axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
# axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')

# axs[0].set_title('Денна', fontsize=10)
# axs[1].set_title('Нічна', fontsize=10)

# fig.suptitle('Температура в м. Полтава', fontsize=15)

# plt.show()

# print("********************************************\n")
# print("""Якщо управляти стилем графіків, то:
# plt.plot(date, [<num>, <num>...], label="...",
# linestyle=": ", color=' ',""")

# date = pd.date_range(start="2021-09-01", freq="D", periods=8)
# plt.figure(figsize=(10, 4))  # Збільшення ширини графіка до 10 дюймів
# plt.plot(
#     date,
#     [23, 17, 17, 16, 15, 14, 17, 20],
#     label="day temperature",
#     linestyle="--",
#     color="#FF5733",
# )
# plt.plot(
#     date,
#     [19, 11, 16, 11, 10, 10, 11, 16],
#     label="night temperature",
#     linestyle="-.",
#     color="#061358",
# )
# plt.xlabel("Дата", fontsize="small", color="midnightblue")
# plt.ylabel("Температура", fontsize="small", color="midnightblue")
# plt.title("Температура в м. Полтава", fontsize=15)
# plt.legend()
# plt.show()
# print("********************************************\n")

# date = pd.date_range(start="2021-09-01", freq="D", periods=8)
# plt.plot(
#     date,
#     [23, 17, 17, 16, 15, 14, 17, 20],
#     label="day temperature",
#     linestyle="-.",
#     color="#FF5733",
#     linewidth=2,
#     marker="D",
# )
# plt.plot(
#     date, # датасет з яким працюємо
#     [19, 11, 16, 11, 10, 10, 11, 16],
#     label="night temperature",
#     linestyle=":", # стиль лінії
#     color="#061358",
#     linewidth=3, # товщина лінії
#     marker="*", # встановлення маркера
# )
# plt.ylim(0, 25) # Остаточне значення
# plt.xlabel("Дата", fontsize="small", color="midnightblue")
# plt.ylabel("Температура", fontsize="small", color="midnightblue")
# plt.title("Температура в м. Полтава", fontsize=15)
# plt.legend()
# plt.grid() # відображення сітки
# plt.show()
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







