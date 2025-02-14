import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


index_data = [1, 2, 3, 4, 5, 6]
data_A = [25, -10, 10, 5, 35, 13]
data_B = [0, 15, -5, 5, 20, 25]
data_C = [10, 25, -15, -15, -5, 15]
df_data = pd.DataFrame({"index_data": index_data,
                       "data_A": data_A, "data_B": data_B, "data_C": data_C})


sns.regplot(x=data_A, y=data_B, data=df_data)
plt.title("A and B")
plt.show()
# -------------------------------------------------

sns.regplot(x=data_A, y=data_C, data=df_data)
plt.title("A and C")
plt.show()
# --------------------------------------------------

sns.regplot(x=data_B, y=data_C, data=df_data)
plt.title("B and C")
plt.show()
