# Working with mixed datatypes (2)
import numpy as np

# Assign the filename: file
file = '../../Datasets/titanic.csv'

# Import file using np.recfromcsv: d
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)

# Print out first three entries of d
print(data[:3])
