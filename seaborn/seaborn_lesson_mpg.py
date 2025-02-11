import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = sns.load_dataset("mpg")
print(f"DataSet named mpg, first 10 line: \n", data.head(10))

sns.set_style('darkgrid')
sns.lineplot(x='model_year', y='horsepower', hue='origin',
             data=data)  # залежність потужності від року випуску

plt.show()

# print("******************************************\n")
