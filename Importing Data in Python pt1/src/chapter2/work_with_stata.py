# Importing Stata files
# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('../../Datasets/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()