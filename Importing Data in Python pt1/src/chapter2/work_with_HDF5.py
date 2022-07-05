# Using h5py to import HDF5 files
# Import packages
import numpy as np
import matplotlib.pyplot as plt
import h5py

# Assign filename: file
file = '../../Datasets/LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))
print("=" * 80)

# Print the keys of the file
for key in data.keys():
    print(key)

print("=" * 80)

# Extracting data from your HDF5 file

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
