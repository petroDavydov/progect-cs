import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# print("******************************************\n")

sns.set_style('whitegrid')

date = pd.date_range(start="2021-01-01", freq="D", periods=8)
day = [23, 17, 17, 16, 15, 14, 17, 20]
night = [19, 11, 16, 11, 10, 10, 11, 16]
df = pd.DataFrame({'date': date, 'day_temperature': day,
                  'night_temperature': night})

sns.lineplot({'day_temperature': day}) # 1 елемент
sns.lineplot(data=df) # всі елементи з DataFrame набору
sns.lineplot(x="night_temperature", y="day_temperature",
             data=df)  # y математичне очікування

sns.lineplot(x="night_temperature", y="day_temperature", data=df,
             sort=False)  # відключення сортування набору даних


plt.show()

print("******************************************\n")
