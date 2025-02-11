import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bestsellers_with_categories.csv")
# print(f"Start DataSet: \n", df)
# print(f"First 5 raw: \n", df.head())
# print(f"Size of DataSet, use shape: \n", df.shape)

df.columns = ['name', 'author', 'user_rating',
              'reviews', 'price', 'year', 'genre']

print(f"Change attribute: \n", df)
# print(f"Count of free space every columns: \n", df.isna().sum())
# print(f"Unique in columns, use unique: \n", df.genre.unique().dtype)
# df.price.plot(kind="hist", title="Price")
# plt.show()

# print(f"Price min: ", df.price.min())
# print(f"Price max: ",df.price.max())
# print(f"Price median: ",df.price.median())
# print(f"Price mean: ",df.price.mean())

print(f"Raiting is the biggest: ", df.user_rating.max())
print(f"Count books with biggest rating: ",
      df[df.user_rating == df.user_rating.max()].shape)

print(f"Book with biggest review: \n", df[df.reviews == df.reviews.max()])
# ----

temp = df[df.year == 2015]
print(f"Middle DataFrame use 2015 year: \n", temp)
print(f"From new dataframe max(): \n", temp[temp.price == temp.price.max()])

print(f"How many books ganre-Fiction, year-2010: \n",
      df[(df.genre == "Fiction") & (df.year == 2010)].shape)


print(f"Rating=4.9 && year=2010,2011: \n",
      df[(df.user_rating == 4.9) & (df.year.isin([2010, 2011]))].shape)

print("Агрегування даних та з'єднання таблиць \n")

print(f"!!!!!! \n", df[["genre", "price"]].groupby(
    "genre").agg(["max", "min"]))


temp1 = df[["name", "author"]].groupby("author").agg('count')

print(f"Size of temp1, use groupby, count, shape: \n", temp1.shape)


print(f"У якого автора найбільше книжок?:  \n",
      temp1[temp1.name == temp1.name.max()])
# ------

temp2 = df[['user_rating', 'author']].groupby('author').agg('mean')
print(f"This is temp2: \n", temp2)
print(f"У якого автора середній рейтинг мінімальний?\
      Який у цього автора середній рейтинг?: \n",
      temp2[temp2.user_rating == temp2.user_rating.min()])
# -----

temp3 = pd.concat([temp1, temp2], axis=1)
print(f"This is temp3: \n", temp3)
temp3.sort_values(['name', 'user_rating'])
print(f"This is temp3 WITH sort_value: \n", temp3)
