import pandas as pd

homelessness = pd.read_csv("../../Datasets/homelessness.csv")

# Print the head of the homelessness data
print()
print("=" * 10 + "Print the head of the homelessness data" + "=" * 10)
print()
print(homelessness.head())


# Print information about homelessness
print()
print("=" * 10 + "Print information about homelessness" + "=" * 10)
print()
print(homelessness.info())

# Print the shape of homelessness
print()
print("=" * 10 + "Print the shape of homelessness" + "=" * 10)
print()
print(homelessness.shape)

# Print a description of homelessness
print()
print("=" * 10 + "Print a description of homelessness" + "=" * 10)
print()
print(homelessness.describe())
