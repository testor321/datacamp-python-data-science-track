import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# avocados = pd.read_pickle("../../Datasets/avoplotto.pkl")
avocados = pd.read_csv("../../Datasets/avocado.csv")

avocados_2016 = avocados[avocados["year"] == 2016]

print(avocados_2016.isna().any())

# simulate NaN
# select only numeric columns to apply the missingness to
# cols_list = avocados_2016.select_dtypes('number').columns.tolist()
cols_list = ["Small Bags", "Large Bags", "XLarge Bags"]

# randomly remove cases from the dataframe
for col in avocados_2016[cols_list]:
    avocados_2016.loc[avocados_2016.sample(frac=0.05).index, col] = np.nan

# List the columns with missing values
cols_with_missing = ["Small Bags", "Large Bags", "XLarge Bags"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# From previous step
cols_with_missing = ["Small Bags", "Large Bags", "XLarge Bags"]
avocados_2016[cols_with_missing].hist()
plt.show()


# From previous step
cols_with_missing = ["Small Bags", "Large Bags", "XLarge Bags"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()
