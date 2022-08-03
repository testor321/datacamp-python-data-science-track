import pandas as pd
import numpy as np

ride_sharing = pd.read_csv("../../Datasets/ride_sharing_v1.csv")

print(ride_sharing.info())
print(ride_sharing.describe())

# Create a tire_size with random seletion of 26, 27, and 29 as the options
# df = pd.DataFrame(np.random.randint(0,100,size=(15, 4)), columns=list('ABCD'))

# ride_sharing['tire_sizes'] = np.random.choice([26,27,29], ride_sharing.shape[0])
# df['column'] = np.random.choice([list of options], ***not sure what the other argument is for***) DTS

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())
