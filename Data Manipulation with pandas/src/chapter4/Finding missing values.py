import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# avocados = pd.read_pickle("../../Datasets/avoplotto.pkl")
avocados = pd.read_csv("../../Datasets/avocado.csv")
print(avocados.describe())

print(avocados.year.unique())
avocados_2016 = avocados[avocados["year"] == 2016]

# print(avocados.describe())
# print(avocados_2016.describe())

# Check individual values for missing values
print("Check individual values for missing values")
print(avocados_2016.isna())

# Check each column for missing values
print("Check each column for missing values")
print(avocados_2016.isna().any())

# simulate NaN
# select only numeric columns to apply the missingness to
# cols_list = avocados_2016.select_dtypes('number').columns.tolist()
cols_list = ["Small Bags", "Large Bags", "XLarge Bags"]

# randomly remove cases from the dataframe
for col in avocados_2016[cols_list]:
    avocados_2016.loc[avocados_2016.sample(frac=0.05).index, col] = np.nan

# TODO
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
#
# See the caveats in the documentation:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   avocados_2016.loc[avocados_2016.sample(frac=0.05).index, col] = np.nan
# Bar plot of missing values by variable


# Bar plot of missing values by variable
print("Bar plot of missing values by variable")
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()
