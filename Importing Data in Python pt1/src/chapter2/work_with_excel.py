# Listing sheets in Excel files
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = '../../Datasets/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print("=" * 80)
print(xl.sheet_names)
print("=" * 80)

# Importing sheets from Excel files
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print("=" * 80)
print(df1.head())
print("=" * 80)

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print("=" * 80)
print(df2.head())
print("=" * 80)

# Customizing your spreadsheet import
# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print("=" * 80)
print(df1.head())
print("=" * 80)

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print("=" * 80)
print(df2.head())
print("=" * 80)
