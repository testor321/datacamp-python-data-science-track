import pandas as pd
import numpy as np

ride_sharing = pd.read_csv("../../Datasets/ride_sharing_v1.csv")

# Create a ride_id with random selection from a range
# ride_sharing['ride_id'] = np.random.choice(np.arange(start=0, stop=500000), ride_sharing.shape[0])

# Strip duration of minutes
# ride_sharing['duration_time'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
# ride_sharing['duration_time'] = ride_sharing['duration_time'].astype('int')


print(ride_sharing.info())
print(ride_sharing.head())

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration_time': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0

