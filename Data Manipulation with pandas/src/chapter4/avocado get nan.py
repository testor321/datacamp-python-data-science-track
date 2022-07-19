import pandas as pd
import numpy as np

# avocados = pd.read_pickle("../../Datasets/avoplotto.pkl")
avocados = pd.read_csv("../../Datasets/avocado.csv")

print(avocados.year.unique())
avocados_2016 = avocados[avocados["year"] == 2016]

print(avocados_2016.describe())

print(avocados_2016.isna().any())

# select only numeric columns to apply the missingness to
# cols_list = avocados_2016.select_dtypes('number').columns.tolist()
cols_list = ["Small Bags", "Large Bags", "XLarge Bags"]

# randomly remove cases from the dataframe
for col in avocados_2016[cols_list]:
    avocados_2016.loc[avocados_2016.sample(frac=0.05).index, col] = np.nan

print(avocados_2016.describe())

print(avocados_2016.isna().any())
