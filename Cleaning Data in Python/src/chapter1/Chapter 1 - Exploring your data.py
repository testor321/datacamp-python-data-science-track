# Chapter 1 - Exploring your data

# Loading and viewing your data
# Import pandas
import pandas as pd
# Import matplotlib.pyplot
import matplotlib.pyplot as plt


# Read the file into a DataFrame: df
df = pd.read_csv('../../Datasets/dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Frequency counts for categorical data
# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

# Visualizing single variables with histograms
# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

print("1" * 80)

# Visualizing multiple variables with boxplots

# Create the boxplot
# df.boxplot(column='Initial Cost', by='Borough')

# Display the plot
# plt.show()

print("2" * 80)

# Visualizing multiple variables with scatter plots
# Create and display the first scatter plot
plt.figure(figsize=(100, 100))
df.plot(kind='scatter', x='Initial Cost', y='Total Est. Fee', rot=70)
plt.show()

print("3" * 80)
