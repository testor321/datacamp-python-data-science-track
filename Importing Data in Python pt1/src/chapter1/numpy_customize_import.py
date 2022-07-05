# Customizing your NumPy import
import numpy as np

# Assign the filename: file
file = '../../Datasets/digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)
