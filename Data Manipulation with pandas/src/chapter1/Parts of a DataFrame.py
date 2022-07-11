# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv("../../Datasets/homelessness.csv")

# Print the values of homelessness
print()
print("=" * 10 + "Print the values of homelessness" + "=" * 10)
print()
print(homelessness.values)

# Print the column index of homelessness
print()
print("=" * 10 + "Print the column index of homelessness" + "=" * 10)
print()
print(homelessness.columns)

# Print the row index of homelessness
print()
print("=" * 10 + "Print the row index of homelessness" + "=" * 10)
print()
print(homelessness.index)
