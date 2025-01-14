# Importing SAS files
from sas7bdat import SAS7BDAT
import matplotlib.pyplot as plt
import pandas as pd

# Save file to a DataFrame: df_sas
with SAS7BDAT('../../Datasets/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


