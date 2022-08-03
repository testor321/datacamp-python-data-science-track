import pandas as pd

ride_sharing = pd.read_csv("../../Datasets/ride_sharing_v1.csv")

# Create a ride_id with random selection from a range
# ride_sharing['ride_id'] = np.random.choice(np.arange(start=0, stop=500000), ride_sharing.shape[0])

# Find duplicates
duplicates = ride_sharing.duplicated(subset='ride_id', keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']].count())
