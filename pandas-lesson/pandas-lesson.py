import pandas as pd
import numpy as np

mountains_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])

print(f"Make simple DataFrame, Series: \n", mountains_height)
print("********************************************\n")

print(f"Add to line - name and dtype\n")

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(f"Add name and dtype to DataFrame: \n", mountains_height, "\n")
print("********************************************\n")

print("Елементи NaN (не число) в об'єкті Series можна замінити       на задане значення, використовуючи метод fillna :\n ")


mountains_height = pd.Series(
    {"Goverla": 2061, "Brebenskyl": 2035.8, "Pip_Ivan": 2028.5},
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(f"Without fillna: \n", mountains_height)

# mountains_height.plot(kind='bar')
# print(mountains_height)


mountains_height.fillna(0, inplace=True)

print(f"Use fillna : \n", mountains_height)
print("********************************************\n")

data = [[1, 'Alice'], [2, 'Bob']]
df = pd.DataFrame(data, columns=['ID', 'Name'])
print(f"This is df from the list: \n ", df)


print("********************************************\n")

data = {'ID': [1, 2], 'Name': ['Alice', 'Bob']}
df = pd.DataFrame(data)

print(f"This is df from the dictionary: \n", df)
print("********************************************\n")

data = np.array([[1, 'Alice'], [2, 'Bob'], [3, 'Jack']])
df = pd.DataFrame(data, columns=['ID', 'Name'])

print(f"This is from array: \n", df)

print("********************************************\n")

data = {'A': [1, 2], 'B': [3, 4], 'C': [8, 9], 'D': ["word", "word"]}
df = pd.DataFrame(data)
print(f"This is shape: \n", df.shape)
print(f"This is columns: \n", df.columns)
print(f"This is index: \n", df.index)
print(f"This is dtypes: \n", df.dtypes)
print("********************************************\n")


contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)

print(contacts)
print("********************************************\n")
print(contacts.loc[1])

contacts.rename(columns={'name': 'Full Name',
                'email': 'Email Address'}, inplace=True)
print(contacts)
print("********************************************\n")

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [np.nan, 5, np.nan]
})

# Застосування методу 'ffill'
df_ffill = df.fillna(method='ffill')

# Застосування методу 'bfill'
df_bfill = df.fillna(method='bfill')

print("Using ffill: \n", df_ffill)

print("\\nUsing bfill: \n", df_bfill)

print("********************************************\n")
